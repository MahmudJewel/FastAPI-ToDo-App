from fastapi import FastAPI
app = FastAPI()
from models import Todos


todo = []
# get all todos 
@app.get("/")
async def get_all_todos():
	return {"Items": todo}

# get single todos 
@app.get("/{id}/")
async def get_single_item(id:int):
	restult = 0
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


# delete todos 



