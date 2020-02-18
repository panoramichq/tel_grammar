#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = 'py-1.0.0'
setup(
    name='tel_grammar_python',
    url='https://github.com/unite-io/tel_grammar/python',
    description='TEL Grammar parser in Python',
    version=VERSION,
    # TODO not sure with following args..
    packages=find_packages(include=['tel_python*']),
    include_package_data=True,
    install_requires=[
        'antlr4-python3-runtime==4.8',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python :: 3.6']
)