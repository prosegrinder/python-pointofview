# -*- coding: utf-8 -*-

"""pointofview

A Python package for determining a piece of text's
point of view (first, second, third, or unknown).
"""

import re
import sys
from collections import OrderedDict

if sys.version_info >= (3, 9):
    from importlib import metadata
else:
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

# Constants for use in comparisons
FIRST = "first"
SECOND = "second"
THIRD = "third"
NONE = None

# NOTE:
# Words are expected to be in lower case.
#
# Point of view is in order of precedence.
# First person PoV can also contain second and third person words.
# Second person PoV can also contain third person words.
# Third person PoV can only contain third person words.
POV_WORDS = OrderedDict(
    [
        (
            FIRST,
            [
                "i",
                "i'm",
                "i'll",
                "i'd",
                "i've",
                "me",
                "mine",
                "myself",
                "we",
                "we're",
                "we'll",
                "we'd",
                "we've",
                "us",
                "ours",
                "ourselves",
            ],
        ),
        (
            SECOND,
            [
                "you",
                "you're",
                "you'll",
                "you'd",
                "you've",
                "your",
                "yours",
                "yourself",
                "yourselves",
            ],
        ),
        (
            THIRD,
            [
                "he",
                "he's",
                "he'll",
                "he'd",
                "him",
                "his",
                "himself",
                "she",
                "she's",
                "she'll",
                "she'd",
                "her",
                "hers",
                "herself",
                "it",
                "it's",
                "it'll",
                "it'd",
                "itself",
                "they",
                "they're",
                "they'll",
                "they'd",
                "they've",
                "them",
                "their",
                "theirs",
                "themselves",
            ],
        ),
    ]
)

RE_WORDS = re.compile(r"[^\w’']+")


def get_word_pov(word, pov_words=None):
    """Get the point-of-view indicated by the word

    Parameters:
    ----------
    word : str
        The English-langauge word to find the point-of-view for

    Returns:
    -------
    str
        the point-of-view indicated by the word (first, second, third)
        returns None if no point-of-view indicated
    """
    if pov_words is None:
        pov_words = POV_WORDS
    for pov in pov_words:
        if word.lower().replace("’", "'") in (
            pov_word.lower() for pov_word in pov_words[pov]
        ):
            return pov
    return None


def parse_pov_words(text, pov_words=None):
    """Parse out all the point-of-view indicator words in text

    Parameters:
    ----------
    text : str
        a block of english languaget text

    Returns:
    -------
    list[str]
        a list of point-of-view indicator words
    """
    if pov_words is None:
        pov_words = POV_WORDS
    text_pov_words = {}
    words = re.split(RE_WORDS, text.strip().lower())
    for pov in pov_words:
        text_pov_words[pov] = []
    for word in words:
        word_pov = get_word_pov(word, pov_words)
        if word_pov is not None:
            text_pov_words[word_pov].append(word)
    return text_pov_words


def get_text_pov(text, pov_words=None):
    """Get the point-of-view of a piece of text

    Parameters:
    ----------
    text : str
        a block of english languaget text

    Returns:
    -------
    str
        the point-of-view of the text (first, second, third)
        returns None if no point-of-view words found
    """
    text_pov_words = parse_pov_words(text, pov_words)
    for pov in POV_WORDS:
        if len(text_pov_words[pov]) > 0:
            return pov
    return None
