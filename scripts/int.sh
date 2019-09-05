#!/bin/bash

docker-compose up -V --no-color --build --abort-on-container-exit
docker-compose down -v
