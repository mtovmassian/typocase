#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import typocase

setup(
    name="typocase",
    version=typocase.__version__,
    packages=find_packages(),
    author="Martin Tovmassian",
    author_email="martin.tovmassian@protonmail.com",
    description=(
        "Lightweight library written in idiomatic Python "
        + "(no regular expressions), that aims to translate string "
        + "into various typography conventions."
    ),
    long_description=open("README.md").read(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Programming tool :: String conversion",
        "License :: MIT",
    ],
)
