# -*- coding: utf-8 -*-
"""
Link Health checker

Known issues:

1) Some websites respond with HTTP 403 but work fine if a link is opened in a
browser manually. There must be advanced request validity checkers doing the job
of rejecting requests sent by bots
(more advanced request header checks and JS tricks).

The only solution would be to upgrade the Link Health script to use
Selenium which does a much better job of emulating a real browser. However, for
simple checking of README pages having few 403 links is fine for our purposes.
This is why the Link Health still uses basic `requests` API.

Examples:

- https://www.fastcompany.com/28121/they-write-right-stuff

2) Some websites open in a browser but don't give any answer when asked by
this script. The result is:
'Connection aborted.', RemoteDisconnected('Remote end closed connection without
response').
"""

import argparse
import multiprocessing
import os
import re
import sys
import yaml
from enum import Enum
from queue import Empty
from typing import Union, List

import requests

__version__ = "0.0.6"


class Parallelizer:
    def __init__(self):
        self.input_queue = multiprocessing.Queue()
        self.output_queue = multiprocessing.Queue()

        self.processes = [
            multiprocessing.Process(
                target=Parallelizer._run,
                args=(self.input_queue, self.output_queue),
            )
            for _ in range(0, multiprocessing.cpu_count())
        ]

        for process in self.processes:
            process.start()

    def __del__(self):
        self.shutdown()

    def shutdown(self):
        for process in self.processes:
            process.terminate()

    @property
    def parallelization_enabled(self):
        return True

    @staticmethod
    def create(parallelize):
        if parallelize:
            return Parallelizer()
        return NullParallelizer()

    def map(self, contents, processing_func):
        size = 0
        for content_idx, content in enumerate(contents):
            self.input_queue.put((content_idx, content, processing_func))
            size += 1
        results = []
        while size > 0:
            try:
                result = self.output_queue.get(block=True, timeout=0.1)
                results.append(result)
                size -= 1
            except Empty:
                if any(process.exitcode for process in self.processes):
                    print(
                        "error: Parallelizer: One of the child processes "
                        "has exited prematurely."
                    )
                    self.shutdown()
                    sys.exit(1)
        return map(lambda r: r[1], sorted(results, key=lambda r: r[0]))

    @staticmethod
    def _run(input_queue, output_queue):
        while True:
            content_idx, content, processing_func = input_queue.get(block=True)
            result = processing_func(content)
            sys.stdout.flush()
            sys.stderr.flush()
            output_queue.put((content_idx, result))


class NullParallelizer:
    @staticmethod
    def map(contents, processing_func):
        results = []
        for content in contents:
            results.append(processing_func(content))
        return results

    def shutdown(self):
        pass

    @property
    def parallelization_enabled(self):
        return False


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

CONNECT_TIMEOUT = 5
READ_TIMEOUT = 5


class Status(str, Enum):
    SUCCESS = "SUCCESS"
    SUCCESS_READ_TIMEOUT_EXPECTED = "SUCCESS_READ_TIMEOUT_EXPECTED"
    HTTP_4xx = "HTTP_4xx"
    HTTP_403 = "HTTP_403"
    HTTP_5xx = "HTTP_5xx"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    SSL_ERROR = "SSL_ERROR"
    CONNECT_TIMEOUT = "CONNECT_TIMEOUT"
    READ_TIMEOUT = "READ_TIMEOUT"

    @staticmethod
    def all():
        return list(map(lambda c: c.value, Status))


class ResponseData:
    def __init__(
        self, link: str, status: Status, payload: Union[None, int, str]
    ):
        self.link: str = link
        self.status: Status = status
        self.payload: Union[None, int, str] = payload
        self.expected = False

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def create_from_response(
        link: str, response: requests.Response
    ) -> "ResponseData":
        if 200 <= response.status_code <= 400:
            return ResponseData(link, Status.SUCCESS, None)
        if 400 <= response.status_code < 500:
            if response.status_code == 403:
                return ResponseData(link, Status.HTTP_403, None)
            return ResponseData(link, Status.HTTP_4xx, None)
        if 500 <= response.status_code < 600:
            return ResponseData(link, Status.HTTP_5xx, None)
        else:
            raise NotImplementedError(response)

    @staticmethod
    def create_from_exception(
        link: str, exception: Exception
    ) -> "ResponseData":
        if isinstance(exception, requests.exceptions.SSLError):
            return ResponseData(link, Status.SSL_ERROR, str(exception))
        if isinstance(exception, requests.exceptions.ReadTimeout):
            return ResponseData(link, Status.READ_TIMEOUT, str(exception))
        if isinstance(exception, requests.exceptions.ConnectTimeout):
            return ResponseData(link, Status.CONNECT_TIMEOUT, str(exception))
        if isinstance(exception, requests.exceptions.ConnectionError):
            return ResponseData(link, Status.CONNECTION_ERROR, str(exception))
        raise NotImplementedError(exception)

    @staticmethod
    def create_from_read_timeout_expected(
        link: str, exception: Exception
    ) -> "ResponseData":
        assert isinstance(exception, requests.exceptions.ReadTimeout)
        return ResponseData(
            link, Status.SUCCESS_READ_TIMEOUT_EXPECTED, str(exception)
        )

    def is_success(self):
        return (
            self.status == Status.SUCCESS
            or self.status == Status.SUCCESS_READ_TIMEOUT_EXPECTED
        )

    def is_ssl_error(self):
        return self.status == Status.SSL_ERROR

    def get_error_message(self):
        payload_string = str(self.payload) if self.payload is not None else ""
        return " ".join([str(self.status), payload_string])

    def get_error_message_with_link(self):
        payload_string = str(self.payload) if self.payload is not None else ""
        return " ".join([str(self.status), payload_string, self.link])

    def promote_to_expected(self):
        self.expected = True


def head_request(link) -> ResponseData:
    try:
        response = requests.head(
            link, timeout=(CONNECT_TIMEOUT, CONNECT_TIMEOUT), headers=HEADERS
        )
        return ResponseData.create_from_response(link, response)
    except Exception as exception:
        return ResponseData.create_from_exception(link, exception)


def get_request(*, link, verify: bool) -> ResponseData:
    try:
        response = requests.get(
            link,
            timeout=(CONNECT_TIMEOUT, READ_TIMEOUT),
            headers=HEADERS,
            verify=verify,
        )
        return ResponseData.create_from_response(link, response)
    except requests.exceptions.ReadTimeout as exception:
        return ResponseData.create_from_read_timeout_expected(link, exception)
    except Exception as exception:
        return ResponseData.create_from_exception(link, exception)


def check_link(link_and_exceptions) -> ResponseData:
    link = link_and_exceptions[0]
    exceptions = link_and_exceptions[1]

    head_response = head_request(link)
    print(".", end="")
    if head_response.is_success():
        return head_response

    if link in exceptions:
        code = exceptions[link]
        if head_response.status.value == code:
            print(
                f"\nHEAD {link} -> Known exception: "
                f"[{head_response.get_error_message()}]"
            )
            head_response.promote_to_expected()
            return head_response

    print(f"\nHEAD {link} [{head_response.get_error_message()}]")

    get_response = get_request(link=link, verify=True)
    if get_response.is_success():
        return get_response

    if get_response.is_ssl_error():
        print(f"\nGET {link} [{get_response.get_error_message()}]", end="\n")
        print(
            f"\nGET {link} – Trying again without SSL verification...", end="\n"
        )

        get_response = get_request(link=link, verify=False)
        if get_response.is_success():
            return get_response

    print(f"\nGET {link} [{get_response.get_error_message()}]", end="\n")

    return get_response


def find_links(input_content):
    return re.findall(r"(?P<url>https?://[^\s><]+[^.\s><])", input_content)


def main():
    parser = argparse.ArgumentParser(description="Description of your program")
    parser.add_argument("input_path")

    args = parser.parse_args()

    input_path = args.input_path
    assert os.path.exists(input_path)

    with open(input_path, "r") as input_file:
        input_content = input_file.read()

    exceptions = {}

    config_file_name = ".link_health.yml"
    if os.path.isfile(config_file_name):
        with open(config_file_name, "r") as stream:
            try:
                config_dict = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                sys.exit(1)
        if "exceptions" in config_dict:
            exceptions_dict = config_dict["exceptions"]
            all_codes = Status.all()
            for exception_dict in exceptions_dict:
                assert "url" in exception_dict
                assert "code" in exception_dict
                exception_code = exception_dict["code"]
                if exception_code not in all_codes:
                    raise Exception(
                        f"Unknown expected error code: {exception_code}. "
                        f"Valid codes: {all_codes}"
                    )
                exceptions[exception_dict["url"]] = exception_code

    links = find_links(input_content)

    parallelizer = Parallelizer()

    link_list = map(lambda el: (el, exceptions), links)
    responses = list(parallelizer.map(link_list, check_link))

    expected_failed_responses: List[ResponseData] = list(
        filter(lambda r: not r.is_success() and r.expected, responses)
    )
    failed_responses: List[ResponseData] = list(
        filter(lambda r: not r.is_success() and not r.expected, responses)
    )

    print("\n")
    for expected_failed_response in expected_failed_responses:
        print(
            f"Expectedly failed link: "
            f"{expected_failed_response.get_error_message_with_link()}"
        )
    for failed_response in failed_responses:
        print(f"Failed link: {failed_response.get_error_message_with_link()}")
    print(
        f"Total links: {len(responses) - len(failed_responses)}, "
        f"failed links: {len(failed_responses)}"
    )
    if len(failed_responses) > 0:
        exit(1)


if __name__ == "__main__":
    main()
