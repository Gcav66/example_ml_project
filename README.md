# This is an ML Project

## Instructions:
* clone repository
* Run `make install` to install dependencies
* Run `make test` to test end-to-end workflow
* 
* Optional: 
 * Run `python run.py` to execute workflow directly
 * Run `uvicorn inference:app --reload --host 0.0.0.0 --port 8001` to serve model on port 8001
 * After serving model (previous command), run `python ml_stuff/models/test_api` to query endpoint

## Overview
Continual helps ML teams bring software engineering practices to ML deployments. This project is a simple example.

* Start with a basic project structure:
 * Code that trains a model (train.py)
 * Code that tests our model (test_train.py)
 * Script that builds and tests our code (Makefile)
 * CI job to automate build & test on merge (GH Action - main.yml)

* The second iteration adds inferencing and Continuous Deployment
 * CD job deploys REST API to AWS ECS on pull request
 * REST API for model inferencing with FastAPI (inference.py)
 * Code that tests our API (test_api.py)
 * Dockerfile to containerize our web service 
 * CD via AWS ECS (GH Action --> ECS Fargate)
 * Right now - this deployment requires manual review by me