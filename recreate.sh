#!/usr/bin/env bash

mkdir -p ./data
docker build -t rpi:rpi /home/gh-actions/rpiapi &&
docker rm --force rpiapi
docker run -d -p [::]:8000:8000 --name rpiapi -v /root/rpiapi/data:/app/data --restart=unless-stopped rpi:rpi
