from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
import sys


class User(BaseModel):
    # Add data model variables

app = FastAPI()
#Load data.json int a list


@app.get("/user", response_model=List[User])
def get_users():
    # Return user list

@app.put("/user/{user_id}", response_model=List[User])
def update_user(user_id: int, user: User):
    # Modify user
    # Return user list

@app.post("/user/", response_model=List[User])
def create_user(user: User):
    # Create new user and append to user list
    # Return user list
