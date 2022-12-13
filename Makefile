install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt &&\
	pip install -e .

test:
	python -m pytest -vv ml_stuff/tests/test_train.py

format:
	black *.py


lint:
	pylint --disable=R,C train.py

all: install lint test

clean:
	rm -rf .env