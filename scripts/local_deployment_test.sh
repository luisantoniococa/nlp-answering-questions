#!/bin/bash
# might need to modify this since I changed the directory
echo "Docker build initializing"

docker build -t testing-fastapi-37-image .

set -a
source local.env
set +a

echo "Docker build finished"
echo "running docker container locally"
echo ${HOST_PORT}
echo ${DOCKER_PORT}
docker run -p ${HOST_PORT}:${DOCKER_PORT} testing-fastapi-37-image


