#!/usr/bin/env bash

mkdir -p ./data
docker build -t rpi:rpi . &&
docker rm --force rpiapi
docker run -d -p [::]:8000:8000 --name rpiapi -v /root/rpiapi/data:/app/data rpi:rpi
