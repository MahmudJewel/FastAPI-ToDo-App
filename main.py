from fastapi import FastAPI
app = FastAPI()

TODO = []
# get all todos 
@app.get("/")
async def home():
	return {"Message": TODO}

# get single todos 


# update todos 


# delete todos 



