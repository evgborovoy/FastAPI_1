from items_views import router as items_router
from users.views import router as users_router
from fastapi import FastAPI

import uvicorn

app = FastAPI()
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def hello_index():
    return {
        "message": "Hello User, it's first app"
    }


@app.get("/hello/")
def hello(name: str, age: int):
    name = name.strip().title()

    return {
        "message": f"hello {name}, you are {age} years old"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
