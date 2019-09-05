#!/bin/bash

docker-compose up -V --no-color --build --abort-on-container-exit

EXIT_CODE=$?

docker-compose down -v

exit $EXIT_CODE
