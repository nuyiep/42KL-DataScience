
.PHONY: build clean

build: clean
	python setup.py sdist bdist_wheel
	pip install ./dist/ft_package-0.0.1.tar.gz

clean:
	rm -rf dist build *.egg-info
	pip uninstall ft_package