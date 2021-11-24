from uuid import uuid4 as uuid
from datetime import datetime
from typing import Text, Optional
from pydantic import BaseModel


# FastAPI
from fastapi import FastAPI,HTTPException


app = FastAPI()
posts = []


# Post MODEL
class Post(BaseModel):
    id : Optional[str]
    title : str
    author : str
    content : Text
    created_at : datetime = datetime.now()
    published_at : Optional[datetime]
    published : bool = False


@app.get('/')
def reas_rooot():
    return {'welcome':'welcome to my API'}


@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts')
def save_posts(post:Post):
    #print(uuid())
    post.id = str(uuid())
    posts.append(post.dict())
    #print(post.dict())
    return posts[-1]


@app.get('/posts/{post_id}')
def get_post(post_id: str):
    #print(post_id)
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code= 404, detail= 'Post Not Found')

