# -*- coding: utf8 -*-

from setuptools import setup, find_packages

def readme():
    with open("README.md", "r") as readme_file:
        return readme_file.read()

EXTRAS = {}

EXTRAS['docs'] = {
    'sphinx'
}

EXTRAS['dev'] = {
    'pylint',
    'pytest',
    'mypy',
    'pytest-cov',
    'codecov'
}

setup(
    # Basic info
    name='pylnd',
    version='0.2.3',
    author='Gabriel Smadi',
    author_email='gabriel@labs.smadi.ci',
    url='https://github.com/smadici-labs/pylnd',
    description='Python client for Lightning Network Deamon',
    long_description=readme(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    install_requires=[
        'requests',
        'grpcio',
        'grpcio-tools',
        'googleapis-common-protos',
    ],
    extras_require=EXTRAS,
    license='MIT',
)
