default:
	@echo "select distinct make action"


# Operam Python base image from Docker Hub
PYTHON_IMAGE_NAME:=operam/base-images:python3.6-latest

VENDOR_NAME:=panoramic
IMAGE_NAME:=tel-grammar
JAVA_IMAGE_NAME_FULL?=$(VENDOR_NAME)/java-$(IMAGE_NAME)
PYTHON_IMAGE_NAME_FULL?=$(VENDOR_NAME)/python-$(IMAGE_NAME)
PYTHON_IMAGE_TESTS_NAME_FULL?=$(VENDOR_NAME)/python-$(IMAGE_NAME)-tests

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


_TEST_IMAGE_MARKER:=/tmp/.$(VENDOR_NAME)-$(IMAGE_NAME)-testrunner-done
$(_TEST_IMAGE_MARKER): python/requirements.txt python/requirements-tests.txt
	docker build \
		-t $(PYTHON_IMAGE_TESTS_NAME_FULL) \
		-f docker/Dockerfile-python-tests .
	touch $(_TEST_IMAGE_MARKER)

test-dev: $(_TEST_IMAGE_MARKER)
	docker run -it --rm \
		-v $(PWD)/python:$(WORKDIR) \
		--workdir ${WORKDIR} \
		$(PYTHON_IMAGE_TESTS_NAME_FULL) \
		pytest -s tests/

# see shipping/Jenkinsfile and keep in sync
test:
	docker run -it --rm \
		-v $(PWD):$(WORKDIR) \
		--workdir ${WORKDIR} \
		python:3.7 \
		bash -c "pip install --upgrade tox && tox -e py37 -c python/tox.ini"
	docker run -it --rm \
		-v $(PWD):$(WORKDIR) \
		--workdir ${WORKDIR} \
		python:3.8 \
		bash -c "pip install --upgrade tox && tox -e py38 -c python/tox.ini"
	docker run -it --rm \
		-v $(PWD):$(WORKDIR) \
		--workdir ${WORKDIR} \
		python:3.9 \
		bash -c "pip install --upgrade tox && tox -e py39 -c python/tox.ini"

.PHONY: test test-dev


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
