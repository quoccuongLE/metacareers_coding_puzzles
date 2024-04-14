#!/bin/bash
VENV_DIR=${1:-".venv/meta_coding"}
conda env create -f conda.yaml --prefix $VENV_DIR
