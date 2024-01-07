from fastapi import FastAPI
app = FastAPI()
from models import Todos

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
async def add_new_item(items:Todos):
	todo.append(items)
	return {"Message": f'Successfully added new items => {items}'}

# update todos  
@app.put("/{id}/")
async def update_item(id:int, items:Todos):
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


