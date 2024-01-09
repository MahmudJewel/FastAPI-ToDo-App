from sqlalchemy.orm import Session
import models, schemas

# get all todos 
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()

# create new todos 

