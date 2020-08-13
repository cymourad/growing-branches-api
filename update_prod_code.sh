#!/usr/bin/env bash

sudo docker-compose down
git pull
sudo docker-compose build
sudo docker-compose up