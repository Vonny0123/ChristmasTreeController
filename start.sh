#!/bin/bash
app="docker.christmas.tree.controller"
docker build -t ${app} .
docker run --privileged -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}
