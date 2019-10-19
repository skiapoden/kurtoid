#!/bin/sh

docker build -t kurtoid --build-arg username="${username}" --build-arg password="${password}" .
