
# FastAPI
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def reas_rooot():
    return {'welcome':'welcome to my API'}


