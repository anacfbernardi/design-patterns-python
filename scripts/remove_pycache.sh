#!/bin/sh

# recursively removes all .pyc files and __pycache__ directories in the current
# directory

cd ..
find ./src | grep -E "(__pycache__|\.pyc$$)" | xargs rm -rf