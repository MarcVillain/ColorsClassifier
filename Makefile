PYTHON        = python3
BIN           = colorsclassifier
OUTPUT        = ~/Downloads/output
IMAGES_FOLDER = ~/Downloads/images

.PHONY: all setup install run run_gui debug debug_gui build_osx format clean

all:
	make run

setup:
	$(PYTHON) -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

install:
	pip install .

upgrade:
	pip install --upgrade --force-reinstall --no-deps .

run:
	$(BIN) --output $(OUTPUT) --images-folder $(IMAGES_FOLDER)

run_gui:
	$(BIN) --output $(OUTPUT) --images-folder $(IMAGES_FOLDER) --gui

debug:
	make upgrade
	$(BIN) --debug --force --output $(OUTPUT) --images-folder $(IMAGES_FOLDER) --method palette --output-type filenames --output-color

debug_gui:
	make upgrade
	$(BIN) --debug --force --output $(OUTPUT) --images-folder $(IMAGES_FOLDER) --method palette --output-type filenames --output-color --gui

build_osx:
	./scripts/build_osx.sh

format:
	black -l 78 colorsclassifier/

clean:
	$(RM) -rf $(OUTPUT) dist/ build/ *.egg-info .eggs
