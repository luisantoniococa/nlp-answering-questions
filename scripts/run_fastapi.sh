#!/bin/bash
set -a
source local.env
set +a

echo "Files in current directory:"
ls 
cd /api_app/app

echo "Files in current directory:"

ls
echo "this are the env variables present"
echo ${DOCKER_PORT}
echo ${HOST_PORT}
uvicorn main:app --host 0.0.0.0 --port ${DOCKER_PORT}