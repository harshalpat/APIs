from typing import Optional

from fastapi import FastAPI

import string
import random
import time

app = FastAPI()

userSession = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/{user_id}/login")
def create_token(user_id: int):
    currentTime = current_milli_time()
    validUntil = currentTime + 600000
    userSession[user_id] = (id_generator(), validUntil)
    return {"user": user_id, "session": userSession[user_id]}


@app.get("/tokens")
def active_token():
    return userSession


def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def current_milli_time():
    return round(time.time() * 1000)
