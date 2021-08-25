# pointofview

[![Latest PyPI version](https://img.shields.io/pypi/v/pointofview.svg)](https://pypi.python.org/pypi/pointofview)
[![GitHub Workflow Status](https://github.com/prosegrinder/python-pointofview/workflows/Python%20CI/badge.svg?branch=main)](https://github.com/prosegrinder/python-pointofview/actions?query=workflow%3A%22Python+CI%22+branch%3Amain)

A Python package for determining a piece of text's point of view (first, second,
third, or unknown).

## Installation

`pointofview` is available on PyPI. Simply install it with `pip`:

```bash
pip install pointofview
```

You can also install it from source:

```bash
$ git clone https://github.com/prosegrinder/python-pointofview.git
Cloning into 'python-pointofview'...
...

$ cd python-pointofview
$ python setup.py install
...
```

## Usage

`pointofview` guesses a text's point of view by counting point of view pronouns.
The main function `get_text_pov()` will return 'first', 'second', 'third', or
null (Python's `None` object):

```python
>>> import pointofview
>>> text = "I'm a piece of text written in first person! What are you?"
>>> pointofview.get_text_pov(text)
'first'
```

There are two other helper functions as well.

`get_word_pov()` returns the point of view of a single word:

```python
>>> pointofview.get_word_pov("I")
'first'
>>> pointofview.get_word_pov("nope")
None
```

`parse_pov_words()` returns a dict containing all first-, second-, and
third-person pov words:

```python
>>> text = """
... When I try to analyze my own cravings, motives, actions and so forth, I surrender to a sort of retrospective imagination which feeds the analytic faculty with boundless alternatives and which causes each visualized route to fork and re-fork without end in the maddeningly complex prospect of my past.
... """
>>> pointofview.parse_pov_words(text)
{'first': ['i', 'i'], 'second': [], 'third': []}
```
