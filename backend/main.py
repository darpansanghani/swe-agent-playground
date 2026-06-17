from fastapi import FastAPI, HTTPException
app = FastAPI()

users_db = {1: {"name": "Alice"}, 2: {"name": "Bob"}}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    # Bug: throws KeyError if user doesn't exist
    return users_db[user_id]
