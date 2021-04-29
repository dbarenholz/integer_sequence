#!/usr/bin/bash
conda env export > environment.yml && exit 0
git add environment.yml
