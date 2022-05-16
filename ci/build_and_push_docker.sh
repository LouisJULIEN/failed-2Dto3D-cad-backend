#!/bin/sh
# first script argument is the docker tag that indicates the version. Defaults to latest.

DOCKER_TAG="${1:-latest}"
FULL_IMAGE_NAME=megacier/small_2dto3d_cad_backend:$DOCKER_TAG

docker build -t $FULL_IMAGE_NAME .
docker image push $FULL_IMAGE_NAME