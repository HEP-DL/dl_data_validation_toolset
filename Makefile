.PHONY: clean clean-build clean-pyc test docs install uninstall help

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -fr .cache/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

test: clean
	pytest --flake8 .

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
