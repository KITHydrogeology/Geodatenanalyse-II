#!/bin/bash

echo "Start environment geo ..."

echo $PWD

source ~/anaconda3/etc/profile.d/conda.sh

conda activate geo

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

jupyter notebook

$SHELL
