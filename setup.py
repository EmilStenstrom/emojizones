# -*- coding: utf-8 -*-
import os

from setuptools import setup

VERSION = '0.1'

setup(
    name='emojizones',
    packages=["emojizones"],
    version=VERSION,
    description='A helper library to convert dates between timezone using emojiis',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    author=u'Emil Stenström',
    author_email='em@kth.se',
    url='https://github.com/EmilStenstrom/emojizones/',
    install_requires=["pytz"],
    keywords=['emojizones', 'conll', 'conll-u', 'parser', 'nlp'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
)
