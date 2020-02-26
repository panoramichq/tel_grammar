default:
	@echo "select distinct make action"


# Operam Python base image from Docker Hub
PYTHON_IMAGE_NAME:=operam/base-images:python3.6-latest

VENDOR_NAME:=panoramic
IMAGE_NAME:=tel-grammar
JAVA_IMAGE_NAME_FULL?=$(VENDOR_NAME)/java-$(IMAGE_NAME)
PYTHON_IMAGE_NAME_FULL?=$(VENDOR_NAME)/python-$(IMAGE_NAME)

WORKDIR=/usr/src/app

image-java:
	docker build \
	    --pull \
		-t $(JAVA_IMAGE_NAME_FULL):latest \
		-f docker/Dockerfile-java .

image-python:
	docker build \
	    --pull \
		-t $(PYTHON_IMAGE_NAME_FULL):latest \
		-f docker/Dockerfile-python .

PHONY: image-java image-python

test: image-python
	docker run --rm ${PYTHON_IMAGE_NAME_FULL}:latest python -m pytest tests


.PHONY: test


build-code-python:
	docker run \
		-v $(PWD):$(WORKDIR) \
		--workdir ${WORKDIR} \
		--rm ${JAVA_IMAGE_NAME_FULL}:latest \
		java -Xmx500M -cp '/usr/local/lib/antlr-4.8-complete.jar:$$CLASSPATH' org.antlr.v4.Tool -visitor -Dlanguage=Python3 -o python/src/tel_grammar/antlr -Xexact-output-dir grammar/Tel.g4

build-code-js:
	docker run \
		-v $(PWD):$(WORKDIR) \
		--workdir ${WORKDIR} \
		--rm ${JAVA_IMAGE_NAME_FULL}:latest \
		java -Xmx500M -cp '/usr/local/lib/antlr-4.8-complete.jar:$$CLASSPATH' org.antlr.v4.Tool -visitor -Dlanguage=JavaScript -o js-temp/ -Xexact-output-dir grammar/Tel.g4

.PHONY: build-code-python

