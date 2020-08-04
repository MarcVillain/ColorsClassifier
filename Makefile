PYTHON   = python3
BIN      = classify.py
OUTPUT   = output

.PHONY: all install run debug format clean

all:
	make run

install:
	$(PYTHON) -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

run:
	$(PYTHON) $(BIN) --output $(OUTPUT) images

debug:
	$(PYTHON) $(BIN) --debug --force --output $(OUTPUT) images

format:
	black -l 78 *.py **/*.py

clean:
	$(RM) -rf $(OUTPUT)
