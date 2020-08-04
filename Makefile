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
	$(PYTHON) $(BIN) --output $(OUTPUT) $(IMAGES_FOLDER)

debug:
	$(PYTHON) $(BIN) --debug --force --output $(OUTPUT) $(IMAGES_FOLDER)

format:
	black -l 78 *.py **/*.py **/**/*.py

clean:
	$(RM) -rf $(OUTPUT)
