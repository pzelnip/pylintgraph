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

echo "Building docker image"
docker build -t matplotlib:latest .

echo "Generating graph"
docker run --rm -v $PWD/output:/tmp matplotlib:latest python3 generate_graph.py

echo "renaming graph"
mv output/pylint.png pylint$1.png

echo "Opening graph"
open output/pylint$1.png
