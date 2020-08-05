#!/bin/bash

log() {
    local message="$1"
    echo "> ${message}"
}

cat <<-EOF
Welcome to the ColorClassifier installer (1.0).
===
Some step require that you type your session password.
The characters you type wont be displayed for more privacy.

Press enter when you are ready to start the installation.
EOF
read -r -n 1
echo "==="

TEMP_DIR="$(mktemp -d)"
log "Creating temporary directory '${TEMP_DIR}'..."
cd "${TEMP_DIR}"

log "Checking dependencies..."
if ! command -v brew &>/dev/null; then
    log "Missing brew dependency. Installing..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    echo "export PATH=/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bash_profile
    source ~/.bash_profile
fi

check_brew_dependency() {
    local command_name="$1"
    local package_name="$2"

    if ! command -v "${command_name}" &>/dev/null; then
        log "Missing ${package_name} dependency. Installing..."
        brew install "${package_name}"
    fi
}
check_brew_dependency python3 python
check_brew_dependency git git
check_brew_dependency fileicon fileicon

log "Downloading repository..."
git clone https://github.com/MarcVillain/ColorsClassifier.git

log "Building the app..."
cd ColorsClassifier/
./scripts/build_osx.sh

log "Moving app to /Applications/ folder..."
mv ./dist/ColorsClassifier.app /Applications/

log "Creating python virtual environment..."
RES_DIR="/Applications/ColorsClassifier.app/Contents/Resources"
mkdir -p "${RES_DIR}"
cd "${RES_DIR}"
python3 -m venv venv
source ./venv/bin/activate

log "Installing colorsclassifier package..."
cd "${TEMP_DIR}/ColorsClassifier"
pip install .

log "Copying resources..."
cp -r "./images" "${RES_DIR}/"

log "Cleaning up..."
cd "${TEMP_DIR}/../"
rm -rf "${TEMP_DIR}"

cat <<-EOF
===
Thank you for your patience, the application is now installed
at this location: ${RES_DIR}

You can start it by right-clicking it then click on "Open".
Click "Open" in the popup. Enjoy.
EOF
