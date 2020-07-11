#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import dirname, join

from setuptools import find_packages, setup


def read_file(file):
    with open(file, "rt") as f:
        return f.read()


with open(join(dirname(__file__), 'my_library/VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()
    

setup(
    name='my_library',
    version=version,
    description='my_library',
    packages=find_packages(exclude=[]),
    author='Jiang Yu',
    author_email='yujiangallen@126.com',
    license='Apache License v2',
    package_data={'': ['*.*']},
    url='https://github.com/walkacross/create-library-from-scratch',
    install_requires=read_file("requirements.txt").strip(),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)