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
APPNAME="Colors Classifier"

# Go to proper worlspace
mkdir -p dist/
cd dist

CONTENTS_DIR="${APPNAME}.app/Contents"
MACOS_DIR="${CONTENTS_DIR}/MacOS"

# Create binary that will setup/start the app
mkdir -p "${MACOS_DIR}"
cp ../scripts/run_app.sh "${MACOS_DIR}/${APPNAME}"
chmod +x "${MACOS_DIR}/${APPNAME}"
fileicon set "Colors Classifier.app" "../images/icon.png"
