# -*- coding: utf-8 -*-

"""pointofview - A Python package for determining a piece of text's point of view (first, second, third, or unknown)."""

import pkg_resources

__version__ = pkg_resources.resource_string(
    'pointofview', 'VERSION').decode('utf-8').strip()

__author__ = 'David L. Day <dday376@gmail.com>'
__all__ = []


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
            "them", "theirs", "themselves"]
}
