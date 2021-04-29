#!/usr/bin/bash
conda env export > environment.yml
git add environment.yml
exit 0
