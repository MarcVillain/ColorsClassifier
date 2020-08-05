#!/bin/bash

CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
RES_DIR="${CUR_DIR}/../Resources"

# Install python3 requirements
if ! command -v python3 &>/dev/null; then
	if ! command -v brew &>/dev/null; then
	    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
	    echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bash_profile
	fi
    brew install python
fi

# Activate python environment
source "${RES_DIR}/venv/bin/activate"
# Run program
APP_IMAGES_FOLDER="${RES_DIR}/images" \
colorsclassifier -g
