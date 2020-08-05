#!/bin/bash

CUR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"
RES_DIR="${CUR_DIR}/../Resources"

# Start
source "${RES_DIR}/venv/bin/activate"
APP_IMAGES_FOLDER="${RES_DIR}/images" \
colorsclassifier --gui
