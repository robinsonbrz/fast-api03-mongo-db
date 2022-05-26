from fastapi import FastAPI

from routes.todos_route import todo_api_router

app = FastAPI(
    title="FastApi com MongoDB Atlas",
    description="API, CRUD inserção de tarefas com persistência MongoDB Atlas",
    version="0.0.1",
    contact={
        "name": "Robinson Enedino",
        "url": "https://www.enedino.com.br",
        "email": "robinsonbrz@gmail.com",
        },
    )

app.include_router(todo_api_router)
