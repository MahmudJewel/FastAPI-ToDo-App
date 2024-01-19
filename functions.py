from fastapi import HTTPException
from sqlalchemy.orm import Session
import models, schemas

# get all todos 
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id:int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return db_todo

# create new todos 
def create_todo(db: Session, todo: schemas.Todos):
    db_todo = models.Todo(item=todo.item)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# update todo 
def update_todo(db: Session, todo_id:int, updated_item: schemas.TodoUpdate):
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_data=updated_item.model_dump(exclude_unset=True) # partial update
    for key, value in updated_data.items():
        setattr(db_todo,key,value)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# delete todo 
def delete_todo(db: Session, todo_id:int):
    db_todo = get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_todo)
    db.commit()
    # db.refresh(db_todo)
    return {"msg": f"Item deleted successfully for {todo_id}"}

