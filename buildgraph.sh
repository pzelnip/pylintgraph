#!/bin/sh

set -e

if [ $# -eq 0 ]
  then
    echo "Must supply build number"
    exit 1
fi

echo "Making output dir"
mkdir -p output

echo "Clearing output dir"
rm output/*

echo "Copying pylint-report.txt to output..."
cp pylint-report.txt output/

echo "Pulling docker image"
docker pull pzelnip/pylintgraph:latest
# to build/push the image:
# docker build -t pzelnip/pylintgraph:latest .
# docker login -u pzelnip
# docker push pzelnip/pylintgraph:latest

echo "Generating graph"
docker run --rm -v $PWD/output:/tmp pzelnip/pylintgraph:latest python3 generate_graph.py

echo "renaming graph"
mv output/pylint.png pylint$1.png

echo "Opening graph"
open pylint$1.png
