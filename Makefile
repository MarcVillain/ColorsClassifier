PYTHON        = python3
BIN           = classify.py
OUTPUT        = output
IMAGES_FOLDER = images

.PHONY: all install run debug format clean

all:
	make run

install:
	$(PYTHON) -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

run:
	$(PYTHON) $(BIN) --output $(OUTPUT) $(IMAGES_FOLDER) --no-gui

debug:
	$(PYTHON) $(BIN) --debug --force --output $(OUTPUT) --images-folder $(IMAGES_FOLDER) -m palette -t filenames -c -n

debug_gui:
	$(PYTHON) $(BIN) --debug --force --output $(OUTPUT) --images-folder $(IMAGES_FOLDER) -m palette -t filenames -c

build_osx:
	./scripts/build_osx.sh

format:
	black -l 78 *.py **/*.py **/**/*.py

clean:
	$(RM) -rf $(OUTPUT) dist/
