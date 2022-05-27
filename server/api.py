from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
    "https://fast-api03-mongo-db.vercel.app",
    "http://localhost",
    "http://localhost:8080",
    "0.0.0.0/0",
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(todo_api_router)
