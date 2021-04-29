#!/usr/bin/bash
# Assumption: This is run from root of project
rm -rf docs
pdoc --force --html --output-dir docs .
mv docs/integer_sequences/* docs/
rmdir docs/integer_sequences/
git add docs
exit 0
