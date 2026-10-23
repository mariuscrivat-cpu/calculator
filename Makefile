PYTHON ?= python3
VENV := .venv
VPY := $(VENV)/bin/python
STAMP := $(VENV)/.installed

.PHONY: start install test

$(STAMP): requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(VPY) -m pip install -r requirements.txt
	touch $(STAMP)

install: $(STAMP)

start: install
	@echo "Calculatorul rulează pe http://$$($(VPY) -c 'from config import load_config as l; c=l(); print("%s:%s" % (c["host"], c["port"]))')"
	$(VPY) app.py

test: install
	$(VPY) -m unittest discover -v -s tests -t .
