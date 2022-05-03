PYTHON := python3
DOCKER := docker

## help: Print this message
.PHONY: help
help:
	@fgrep -h '##' $(MAKEFILE_LIST) | fgrep -v fgrep | column -t -s ':' | sed -e 's/## //'

## run: Run the app locally 
.PHONY: run
run:
	$(PYTHON) main.py 

## docker-build: Build the docker image 
.PHONY: docker-build
docker-build:
	@echo "Not Implemented Yet"

## docker-run: Run the built docker image
.PHONY: docker-run
docker-run:
	@echo "Not Implemented Yet..."
