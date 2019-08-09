FROM python:3.7-slim-stretch

ADD . /pylnd

WORKDIR /pylnd

RUN pip install -e .[dev]

RUN python setup.py develop

RUN pytest
