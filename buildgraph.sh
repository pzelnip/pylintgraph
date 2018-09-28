#!/bin/sh

set -e

echo "Making output dir"
mkdir -p output

echo "Copying pylint-report.txt to output..."
cp pylint-report.txt output/

echo "Building docker image"
docker build -t matplotlib:latest .

echo "Generating graph"
docker run --rm -v $PWD/output:/tmp matplotlib:latest python3 generate_graph.py

echo "Opening graph"
open output/pylint.png
