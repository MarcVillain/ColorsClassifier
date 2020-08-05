#!/bin/bash

CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
RES_DIR="${CUR_DIR}/../Resources"

if [ ! -d "${RES_DIR}" ]; then
    # Install

    if [ ! command -v brew >/dev/null 2>&1 ]; then
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bash_profile
    fi

    if [ ! command -v python3 >/dev/null 2>&1 ]; then
        brew install python
    fi

    if [ ! command -v git >/dev/null 2>&1 ]; then
        brew install git
    fi

    mkdir -p "${RES_DIR}"
    cd "${RES_DIR}"

    git clone git@github.com:MarcVillain/ColorClassifier.git

    python3 -m venv venv
    source venv/bin/activate

    cd ColorClassifier/
    pip install -r requirements.txt
fi

# Start
source "${RES_DIR}/venv/bin/activate"
python "${RES_DIR}/ColorClassifier/classify.py"
