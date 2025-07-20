# -*- coding: utf-8 -*-

"""pointofview

A Python package for determining a piece of text's
point of view (first, second, third, or unknown).
"""

import re
import sys
from typing import Literal, OrderedDict

from importlib import metadata

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
POV_WORDS: OrderedDict[str, list[str]] = OrderedDict(
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


def get_word_pov(
    word: str, pov_words: OrderedDict[str, list[str]] | None = None
) -> str | None:
    """Get the point-of-view indicated by the word

    Parameters:
    ----------
    word : str
        The English-langauge word to find the point-of-view for

    pov_words : dict, optional
        A dictionary of point-of-view words to use for comparison.
        If None, the default POV_WORDS will be used.

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


def parse_pov_words(
    text: str, pov_words: OrderedDict[str, list[str]] | None = None
) -> OrderedDict[str, list[str]]:
    """Parse out all the point-of-view indicator words in text

    Parameters:
    ----------
    text : str
        a block of english language text

    pov_words : dict, optional
        A dictionary of point-of-view words to use for comparison.
        If None, the default POV_WORDS will be used.

    Returns:
    -------
    list[str]
        a list of point-of-view indicator words
    """
    if pov_words is None:
        pov_words = POV_WORDS
    text_pov_words: OrderedDict[str, list[str]] = OrderedDict()
    words: list[str] = re.split(RE_WORDS, text.strip().lower())
    for pov in pov_words:
        text_pov_words[pov] = []
    for word in words:
        word_pov = get_word_pov(word, pov_words)
        if word_pov is not None:
            text_pov_words[word_pov].append(word)
    return text_pov_words


def get_text_pov(
    text: str, pov_words: OrderedDict[str, list[str]] | None = None
) -> str | None:
    """Get the point-of-view of a piece of text

    Parameters:
    ----------
    text : str
        a block of english language text

    pov_words : dict, optional
        A dictionary of point-of-view words to use for comparison.
        If None, the default POV_WORDS will be used.

    Returns:
    -------
    str
        the point-of-view of the text (first, second, third)
        returns None if no point-of-view words found
    """
    text_pov_words: OrderedDict[str, list[str]] = parse_pov_words(text, pov_words)
    for pov in POV_WORDS:
        if len(text_pov_words[pov]) > 0:
            return pov
    return None
