Content Organization
====================

It is not a trivial task to organize content of such a resource in a meaningful
way. With the growth of the awesome-safety-critical, the organization of the
content has been changing a number of times and since the resource grows
constantly, more changes in how the content is organized are expected too.

This page explains the current principles and techniques that are used for
the content organization.

- awesome-safety-critical is a single-page list document.

- Content is sorted by types which are H2 sections: standards are in Standards,
  papers are in Papers, videos are in Videos, etc.

  - Exception: content that strongly gravitates to a separate dedicated topic.
    Example: MC/DC test coverage.

- The content of
  `awesome-safety-critical <https://github.com/stanislaw/awesome-safety-critical>`_
  is hosted on GitHub. It is generated using Sphinx and
  `Read the Docs <readthedocs.io>`_ into HTML pages (this website).

- The content is written in reStructuredText (RST) format. This is done to
  overcome the limitation of the Markdown format that does not support adding
  meta information to the content.

Tags and meta information
-------------------------

Tags are supposed to help in navigating the content. Using RST syntax and
the capabilities of Sphinx that allow creation of custom RST content, each link
has associated meta information and from this information the tags and the
filtering functionality based on it are produced.

Typical link example:

.. code-block:: RST

  .. asc-meta::
      :types: Book
      :keywords: Safety, System Safety
      :industries: All
      :people: Nancy Leveson

      `Engineering a Safer World. Systems Thinking Applied to Safety
      <https://mitpress.mit.edu/books/engineering-safer-world>`_

Aliases
~~~~~~~

Some links can be associated with the keywords or topics that may be similar.
This might produce duplication and possibly confusion.

The following are the current rules used for aliasing:

``Formal methods, Formal verification`` are aliased to ``Formal verification``

``Aerospace`` is aliased to either ``Space`` or ``Aviation`` depending on
whereto it gravitates more.

``Avionics`` is aliased to ``Aviation``. Unless it has a sense of electronics
onboard an aircraft or a spacecraft which has not been the case so far.

There are more implicit rules for aliasing of this kind. Depending on the new
content they might change if it is clear that alternative naming yields more
consistent results.
