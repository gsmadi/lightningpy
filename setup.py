# -*- coding: utf8 -*-

import os

from setuptools import setup, find_packages
    
setup(
    # Basic info
    name='pylnd',
    version='0.1.0',
    author='Gabriel Smadi',
    author_email='gabriel@labs.smadi.ci',
    url='https://github.com/smadici-labs/pylnd.git',
    description='Python client for Lightning Network Deamon',

    install_requires=[
        'requests',
        'grpcio',
        'grpcio-tools',
        'googleapis-common-protos',
        'pylint',
        'pytest',
        'mypy'
    ],
)