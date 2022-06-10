PYTHON := python3
DOCKER := docker

DOCKER_IMAGE_NAME := coder-value

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
	$(DOCKER) build \
		-t $(DOCKER_IMAGE_NAME) \
		.

## docker-run: Run the built docker image
.PHONY: docker-run
docker-run:
	$(DOCKER) run \
		--rm \
		-w /app \
		-p 5000:5000 \
		$(DOCKER_IMAGE_NAME):latest

