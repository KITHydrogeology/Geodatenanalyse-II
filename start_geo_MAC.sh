#!/bin/bash

echo "Starting environment geo ..."

echo $PWD

source /opt/anaconda3/etc/profile.d/conda.sh

conda activate geo

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

jupyter notebook

$SHELL