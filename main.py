
# FastAPI
from fastapi import FastAPI


app = FastAPI()
posts = []

@app.get('/')
def reas_rooot():
    return {'welcome':'welcome to my API'}


@app.get('/posts')
def get_posts():
    return posts
