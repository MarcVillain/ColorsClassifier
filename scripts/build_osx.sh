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

# Create app structure
mkdir -p "${MACOS_DIR}"

# Add startup script
cp "scripts/run_osx.sh" "${MACOS_DIR}/${APP_NAME}"
chmod +x "${MACOS_DIR}/${APP_NAME}"

# Add Info.plist
cp "scripts/Info.plist" "${CONTENTS_DIR}"

# Add icon
fileicon set "${APP_DIR}" "images/icon.png"
