.PHONY: clean  clean-build clean-pyc docs help

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

lint:
	flake8 dl_data_validation_toolset tests

flake: 
	flake8 .

test: flake
	pytest

docs:
	rm -f docs/dl_data_validation_toolset.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ dl_data_validation_toolset
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

install: clean
	python setup.py install

uninstall:
	pip uninstall dl_data_validation_toolset