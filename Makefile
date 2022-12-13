install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt &&\
	pip install -e .

lint:
	pylint --disable=R,C ml_stuff/models/train.py

format:
	black ml_stuff/tests/*.py
	black ml_stuff/models/*.py
	black ml_stuff/data/*.py

test:
	python -m pytest -vv ml_stuff/tests/test_train.py