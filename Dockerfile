FROM python:3.9
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src_data /code/src_data
COPY ./ml_stuff /code/ml_stuff
COPY ./Makefile /code/Makefile
COPY ./run.py /code/run.py
COPY .github/workflows /code/.github/workflows
COPY ./setup.py /code/setup.py
RUN pip install -e /code/.

# 
#COPY ./app /code/app

# 
CMD ["uvicorn", "ml_stuff.models.inference:app", "--host", "0.0.0.0", "--port", "8001"]
