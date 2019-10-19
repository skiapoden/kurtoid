#!/bin/sh

docker build -t kurtoid --build-arg GITLAB_USERNAME="${GITLAB_USERNAME}" GITLAB_PASSWORD="${GITLAB_PASSWORD}" .
docker run -it --rm --name kurtoidapp -p 5000:5000 kurtoid
