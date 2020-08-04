#!/usr/bin/env python
import os

from setuptools import find_packages, setup


VERSION = '1.0.8'
setup(
    name='tel_grammar',
    description='TEL Grammar parser in Python',
    url='https://github.com/unite-io/tel_grammar/python',
    project_urls={'Source Code': 'https://github.com/unite-io/tel_grammar/python'},
    author="Panoramic",
    maintainer="Panoramic",
    keywords=["grammar", "taxonomy"],
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=['antlr4-python3-runtime==4.8'],
    extras_require={"tests": ["pytest>=5.3.5"], "dev": ["pytest>=5.3.5", "pre-commit>=2.1.1"]},
    include_package_data=True,
)
