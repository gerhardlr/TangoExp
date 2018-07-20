#!/usr/bin/env bash
export DOCKER_NETWORK=docker-network

cd dev/
export DEV_HOME=$(pwd)
cd ..

docker-compose -f docker-compose.dev.yml up -d