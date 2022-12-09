install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_train.py

format:
	black *.py


lint:
	pylint --disable=R,C train.py

all: install lint test