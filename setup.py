# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

# Version
with open(path.join(path.dirname(__file__), 'pointofview', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()
# Long Description
with open(path.join(path.dirname(__file__), 'README.rst')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()


setup(
    name="pointofview",
    version=VERSION,
    url="https://github.com/prosegrinder/python-pointofview",

    author="David L. Day",
    author_email="dday376@gmail.com",

    description="A Python package for determining a piece of text's point of view (first, second, third, or unknown).",
    long_description=LONG_DESCRIPTION,

    packages=[
        'pointofview'
    ],
    package_dir={'pointofview': 'pointofview'},
    package_data={
        '': ['LICENSE', '*.rst', 'MANIFEST.in'],
    },
    include_package_data=True,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
