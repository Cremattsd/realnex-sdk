#!/bin/bash
# This script will be executed during the build phase

# Print out the current directory to verify where the script is running
echo "Current directory: $(pwd)"

# List the files in the current directory to verify the files are present
echo "Listing files in current directory:"
ls -al

# Check if the README.md file exists (because the error you're encountering is related to it)
echo "Checking if README.md exists:"
ls -al README.md

# If everything is good, proceed with building the project using setuptools
echo "Running setup.py to build the package:"
python3 setup.py sdist bdist_wheel

# Ensure the build was successful
if [ $? -eq 0 ]; then
    echo "Build succeeded!"
else
    echo "Build failed!"
    exit 1
fi
