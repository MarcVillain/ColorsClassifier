#!/bin/bash

CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
RES_DIR="${CUR_DIR}/../Resources"

# Due to the weird way I am building this app manually,
# I need to have the virtualenv created in the proper
# location for this to work and not have files spread
# through the files of the user.
#
# It can seem annoying but it is the only way I can make
# it work as of now so that this can be installed simply
# by running a single command for all types of users.
if ! grep "Application"; then
    osascript -e 'tell app "System Events" to display dialog "Please place this app in your Applications/ folder before trying to install it."'
    exit 1
fi

if [ ! -d "${RES_DIR}" ]; then
    # Install
    if ! command -v brew &>/dev/null; then
        echo "This step requires you to type your session password."
        echo "The characters you type wont be displayed for more privacy."
        ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
        echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bash_profile
    fi

    if ! command -v python3 &>/dev/null; then
        brew install python
    fi

    if ! command -v git &>/dev/null; then
        brew install git
    fi

    mkdir -p "${RES_DIR}"

    cd "${RES_DIR}"
    python3 -m venv venv
    source venv/bin/activate
    cd -

    git clone git@github.com:MarcVillain/ColorClassifier.git
    cd ColorClassifier/
    pip install .
    cd -
fi

# Start
source "${RES_DIR}/venv/bin/activate"
colorsclassifier
