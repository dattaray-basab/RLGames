all: clean build

clean:
	pip freeze | xargs pip uninstall -y

build:
	pip install -r requirements.txt
