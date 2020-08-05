#!/bin/bash

# ==============================================================================
# INFORMATION
# ==============================================================================
# Unfortunately, I am using packages that are not yet compatible with py2app
# that would have helped with building this app.
#
# Therefore, I am writing that script to build everything by hand, in hope
# that it will be easier to use and maintain.
# ==============================================================================

# Configuration variables
APP_NAME="ColorsClassifier"
APP_DIR="dist/${APP_NAME}.app"
CONTENTS_DIR="${APP_DIR}/Contents"
MACOS_DIR="${CONTENTS_DIR}/MacOS"
RES_DIR="${CONTENTS_DIR}/Resources"
APP_FILE="${MACOS_DIR}/${APP_NAME}"

if [ "${1}" == "--clean" ]; do
    rm -rf "${APP_DIR}"
fi

# If nothing was already built
if [ ! -d "${APP_DIR}" ]; then
    # Create workspace
    mkdir -p "${MACOS_DIR}"
    mkdir -p "${RES_DIR}"
    # Add "binary"
    cp scripts/run_app.sh "${APP_FILE}"
    chmod +x "${APP_FILE}"
    # Set icon
    fileicon set "${APP_DIR}" "images/icon.png"
    # Create and activate virtualenv
    cd "${RES_DIR}"
    python3 -m venv venv
    source venv/bin/activate
    cd -
    # Install Colors-Classifier package
    pip install -r requirements.txt
    pip install .

# Update sources only
else
    source "${RES_DIR}/venv/bin/activate"
    pip install --upgrade --force-reinstall --no-deps .
fi
