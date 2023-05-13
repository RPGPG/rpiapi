#!/usr/bin/env bash

mkdir -p ./data
cd /home/gh-actions/rpiapi && docker build -t rpi:rpi . &&
docker rm --force rpiapi
docker run -d -p [::]:8000:8000 --name rpiapi -v /home/gh-actions/rpiapi/data:/app/data --restart=unless-stopped rpi:rpi
