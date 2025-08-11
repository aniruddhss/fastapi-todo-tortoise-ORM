from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
import os


app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI and Tortoise ORM",
    version="1.0.0"
)
app.include_router(todo_router)

# Database configuration
db_path = os.path.join(os.getcwd(), "todo.db")
db_url = f"sqlite://{db_path}"

register_tortoise(
    app=app,
    db_url=db_url,
    add_exception_handlers=True,
    generate_schemas=True,
    modules={"models":["api.models.modeltodo"]}
)


@app.get("/")
def index():
    return {"status":"ToDo api is running", "docs": "/docs", "redoc": "/redoc"}