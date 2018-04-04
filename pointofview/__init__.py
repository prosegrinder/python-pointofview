# -*- coding: utf-8 -*-

"""pointofview - A Python package for determining a piece of text's point of view (first, second, third, or unknown)."""

import re
from collections import OrderedDict

import pkg_resources

__version__ = pkg_resources.resource_string(
    'pointofview', 'VERSION').decode('utf-8').strip()

# NOTE: Point of view is in order of precedence.
# First person PoV can also contain second and third person words.
# Second person PoV can also contain third person words.
# Third person PoV can only contain third person words.
POV_WORDS = OrderedDict([
    ('first',
        ["i", "i'm", "i'll", "i'd", "i've", "me", "mine", "myself", "we",
            "we're", "we'll", "we'd", "we've", "us", "ours", "ourselves"]),
    ('second',
        ["you", "you're", "you'll", "you'd", "you've",
            "your", "yours", "yourself", "yourselves"]),
    ('third',
        ["he", "he's", "he'll", "he'd", "him", "his", "himself", "she", "she's",
            "she'll", "she'd", "her", "hers", "herself", "it", "it's", "it'll",
            "it'd", "itself", "they", "they're", "they'll", "they'd", "they've",
            "them", "their", "theirs", "themselves"])
])

RE_WORDS = re.compile(r"[^\w’']+")


def _normalize_word(word):
    return word.strip().lower().replace("’", "'")


def get_word_pov(word, pov_words=POV_WORDS, normalize_words=True):
    if normalize_words:
        word = _normalize_word(word)
    for pov in pov_words:
        if word in pov_words[pov]:
            return pov
    return None


def parse_pov_words(text, pov_words=POV_WORDS, normalize_words=True):
    text_pov_words = {}
    words = re.split(RE_WORDS, text.strip().lower())
    for pov in pov_words:
        text_pov_words[pov] = []
    for word in words:
        word_pov = get_word_pov(word, pov_words, normalize_words)
        if word_pov != None:
            text_pov_words[word_pov].append(word)
    return text_pov_words


def get_text_pov(text, pov_words=POV_WORDS, normalize_words=True):
    text_pov_words = parse_pov_words(text, pov_words, normalize_words)
    for pov in POV_WORDS:
        if len(text_pov_words[pov]) > 0:
            return pov
    return None
