from pydantic import BaseModel

class Todos(BaseModel):
    id : int
    item : str

class TodoCreate(Todos):
    pass
