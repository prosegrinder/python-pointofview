# -*- coding: utf-8 -*-

"""pointofview - A Python package for determine a text's point of view (first, second, third, or unknown)."""

import pkg_resources

__version__ = pkg_resources.resource_string(
    'pointofview', 'VERSION').decode('utf-8').strip()

__author__ = 'David L. Day <dday376@gmail.com>'
__all__ = []
