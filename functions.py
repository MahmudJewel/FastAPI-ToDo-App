from sqlalchemy.orm import Session
import models, schemas

# get all todos 
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()
def get_todo(db: Session, tod_id:int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == tod_id).first()
    return db_todo

# create new todos 
def create_todo(db: Session, todo: schemas.Todos):
    db_todo = models.Todo(item=todo.item)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
