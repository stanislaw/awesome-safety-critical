import argparse
import multiprocessing
import os
import re
import requests
import sys

from typing import Union
from queue import Empty

__version__ = "0.0.1"


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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

CONNECT_TIMEOUT = 5
READ_TIMEOUT = 5


def head_request(link) -> Union[requests.Response, Exception]:
    try:
        r = requests.head(link, timeout=(CONNECT_TIMEOUT, CONNECT_TIMEOUT), headers=HEADERS)
        return r
    except requests.exceptions.ReadTimeout as exception:
        return exception
    except requests.exceptions.ConnectTimeout as exception:
        return exception
    except requests.exceptions.ConnectionError as exception:
        return exception


def get_request(link) -> Union[requests.Response, bool, Exception]:
    try:
        r = requests.get(link, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT), headers=HEADERS)
        return r
    except requests.exceptions.ReadTimeout:
        return True
    except requests.exceptions.ConnectTimeout as exception:
        return exception
    except requests.exceptions.ConnectionError as exception:
        return exception
    except Exception:
        raise NotImplementedError


def check_link(link) -> Union[requests.Response, Exception]:
    head_response = head_request(link)
    print(".", end="")
    if isinstance(head_response, requests.Response) and head_response.status_code < 400:
        return head_response

    error_message = (
        head_response.status_code if isinstance(head_response, requests.Response)
        else head_response
    )
    print(f"\nHEAD {link} [{error_message}]")

    get_response = get_request(link)
    if isinstance(get_response, requests.Response):
        if get_response.status_code < 400:
            return get_response
        print(f"GET {link} [{get_response.status_code}]", end="")
    else:
        print(f"GET {link} [{get_response}]", end="")
    return get_response


def main():
    parser = argparse.ArgumentParser(description='Description of your program')
    parser.add_argument("input_path")

    args = parser.parse_args()

    input_path = args.input_path
    assert os.path.exists(input_path)

    with open(input_path, "r") as input_file:
        input_content = input_file.read()

    links = re.findall(r"(?P<url>https?://[^\s><]+)", input_content)

    parallelizer = Parallelizer()

    responses = list(parallelizer.map(links, check_link))
    print("")
    failed_responses = list(filter(
        lambda response: isinstance(response, Exception), responses
    ))
    for failed_response in failed_responses:
        print(f"Failed link: {failed_response}")
    print(
        f"Total links: {len(responses) - len(failed_responses)}, "
        f"failed links: {len(failed_responses)}"
    )
    if len(failed_responses) > 0:
        exit(1)


if __name__ == '__main__':
    main()
