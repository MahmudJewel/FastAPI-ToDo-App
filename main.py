from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

# from . import crud, models, schemas
import models, schemas, functions
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =============> todo using list <=====================
todo = []

# get all todos 
@app.get("/")
async def get_all_items():
	return {"Items": todo}

# get single todos 
@app.get("/{id}/")
async def get_single_item(id:int):
	for item in todo:
		if item.id == id:
			return item
	return {"message": "Item not found"}

# create new todos 
@app.post("/")
async def add_new_item(items:schemas.Todos):
	todo.append(items)
	return {"Message": f'Successfully added new items => {items}'}

# update todos  
@app.put("/{id}/")
async def update_item(id:int, items:schemas.Todos):
	for obj in todo:
		if obj.id == id:
			obj.id = id
			obj.item = items.item
			return {"messages": f"Successfully updated item => {obj}"}
	return {"message": "Item not found to update"}

# delete todos 
@app.delete("/{id}/")
async def delete_item(id:int):
	for item in todo:
		if item.id == id:
			todo.remove(item)
			return {"message": f"Item deleted successfully => {item}"}
	return {"message": "Item not found to remove"}

# ============== todo using db ===============

# create new todos 
@app.post("/todo/", response_model=schemas.AllTodos)
async def create_new_todo(item: schemas.Todos, db: Session = Depends(get_db)):
	return functions.create_todo(db=db, todo=item)

# get all todos 
@app.get("/todo", response_model=list[schemas.AllTodos])
async def get_all_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	items = functions.get_todos(db=db, skip=skip, limit=limit)
	return items

# get todo by id
@app.get("/todo/{todo_id}",response_model=schemas.AllTodos)
async def get_todo(todo_id:int, db: Session = Depends(get_db)):
	item = functions.get_todo(db=db, todo_id=todo_id)
	if item is None:
		raise HTTPException(status_code=404, detail="Item not found")
	return item

# update todo
@app.patch("/todo/{todo_id}", response_model=schemas.AllTodos)
async def update_todo(tod_id:int, updated_item: schemas.TodoUpdate, db: Session = Depends(get_db)):
	item = functions.update_todo(db=db, todo_id=todo_id, updated_item=updated_item)
	return item

# update todo
@app.delete("/todo/{todo_id}")
async def delete_todo(todo_id:int, db: Session = Depends(get_db)):
	item = functions.delete_todo(db=db, todo_id=todo_id)
	return item