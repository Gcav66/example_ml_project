from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib

app = FastAPI(title="Continual ML Example")

model = load(pathlib.Path('ml_stuff/models/model_store/clf_v1.joblib'))

class InputData(BaseModel):
    med_inc:int=34
    house_age:int=13 
    ave_rooms:int=7
    ave_bdms:int=1
    pop:int=1
    ave_occup:int=752
    lat:float=2.79
    long:float=39.02

class OutputData(BaseModel):
    score:float=0.7353634

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict(model_input)[0]
    
    return {'score':result}

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
