from pydantic import BaseModel

class Todos(BaseModel):
    item: str

class TodoCreate(Todos):
    completed: bool

class TodoUpdate(TodoCreate):
    pass

class AllTodos(Todos):
    id: int
    completed: bool
    class Config:
        orm_mode = True

