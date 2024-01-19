from pydantic import BaseModel, ConfigDict

class Todos(BaseModel):
    item: str

class TodoCreate(Todos):
    pass

class AllTodos(Todos):
    id: int
    completed: bool

    class Config:
        orm_mode = True

