install:
	source .env/bin/activate &&\
	pip install --upgrade pip &&\
	pip install -r requirements.txt &&\
	pip install -e .

test:
	python -m pytest -vv test_train.py

format:
	black *.py


lint:
	pylint --disable=R,C train.py

all: install lint test