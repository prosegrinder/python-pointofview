# -*- coding: utf-8 -*-

"""pointofview - A Python package for determining a piece of text's point of view (first, second, third, or unknown)."""

import re

import pkg_resources

__version__ = pkg_resources.resource_string(
    'pointofview', 'VERSION').decode('utf-8').strip()

POV_WORDS = {
    'first':
        ["i", "i'm", "i'll", "i'd", "i've", "me", "mine", "myself", "we",
            "we're", "we'll", "we'd", "we've", "us", "ours", "ourselves"],
    'second':
        ["you", "you're", "you'll", "you'd", "you've",
            "your", "yours", "yourself", "yourselves"],
    'third':
        ["he", "he's", "he'll", "he'd", "him", "his", "himself", "she", "she's",
            "she'll", "she'd", "her", "hers", "herself", "it", "it's", "it'll",
            "it'd", "itself", "they", "they're", "they'll", "they'd", "they've",
            "them", "their", "theirs", "themselves"]
}

RE_WORDS = re.compile(r"[^\w’']+")


def _normalize_word(word):
    return word.strip().lower().replace("’", "'")


def get_word_pov(word):
    for pov in POV_WORDS:
        if _normalize_word(word) in POV_WORDS[pov]:
            return pov
    return None


def parse_pov_words(text):
    pov_words = {
        'first': [],
        'second': [],
        'third': [],
    }
    words = re.split(RE_WORDS, text.strip().lower())
    for word in words:
        pov = get_word_pov(word)
        if pov != None:
            pov_words[pov].append(word)
    return pov_words


def get_pov(text):
    pov_words = parse_pov_words(text)
    if len(pov_words['first']) > 0:
        return 'first'
    elif len(pov_words['second']) > 0:
        return 'second'
    elif len(pov_words['third']) > 0:
        return 'third'
    else:
        return None
