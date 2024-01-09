from sqlalchemy.orm import Session
import models, schemas

# get all todos 
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

# create new todos 
def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(item=todo.item)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
