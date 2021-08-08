pointofview
===========

.. image:: https://img.shields.io/pypi/v/pointofview.svg
    :target: https://pypi.python.org/pypi/pointofview
    :alt: Latest PyPI version

.. image:: https://github.com/prosegrinder/python-pointofview/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/prosegrinder/python-pointofview/actions?query=workflow%3A%22Python+CI%22+branch%3Amain
    :alt: GitHub Workflow Status

.. image:: https://api.codacy.com/project/badge/Grade/df0afcc70ffc4a86a8777588567820c0
    :target: https://www.codacy.com/app/ProseGrinder/python-pointofview?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=prosegrinder/python-pointofview&amp;utm_campaign=Badge_Grade
    :alt: Latest Codacy Coverage Report

A Python package for determining a piece of text's point of view (first, second, third, or unknown).

Installation
------------

``pointofview`` is available on PyPI. Simply install it with ``pip``::

    $ pip install pointofview

You can also install it from source::

    $ git clone https://github.com/prosegrinder/python-pointofview.git
    Cloning into 'python-pointofview'...
    ...

    $ cd python-pointofview
    $ python setup.py install
    ...

Usage
-----

``pointofview`` guesses a text's point of view by counting point of view pronouns. The main function ``get_text_pov()`` will return 'first', 'second', 'third', or null (Python's ``None`` object)::

    >>> import pointofview
    >>> text = "I'm a piece of text written in first person! What are you?"
    >>> pointofview.get_text_pov(text)
    'first'

There are two other helper functions as well.

``get_word_pov()`` returns the point of view of a single word::

    >>> pointofview.get_word_pov("I")
    'first'
    >>> pointofview.get_word_pov("nope")
    None

``parse_pov_words`` returns a dict containing all first, second, and third person pov words::

    >>> text = """
    ... When I try to analyze my own cravings, motives, actions and so forth, I surrender to a sort of retrospective imagination which feeds the analytic faculty with boundless alternatives and which causes each visualized route to fork and re-fork without end in the maddeningly complex prospect of my past.
    ... """
    >>> pointofview.parse_pov_words(text)
    {'first': ['i', 'i'], 'second': [], 'third': []}

Authors
-------

`pointofview` was written by `David L. Day <dday376@gmail.com>`_.
