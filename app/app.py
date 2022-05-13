from fastapi import FastAPI

todos = [
    {
        "id" : 1,
        "task" : "LeetCode Daily Challenge"
    },
    {
        "id" : 2,
        "task" : "Leetcode Weekly Contest"
    }
]

# {
#     "id" : 3,
#     "task" : "LeetCode Biweekly Contest"
# }

app = FastAPI()

@app.get("/", tags=["root"])
# async is optional here
async def root() -> dict:
    return {"message" : "Hello World!"}

@app.get("/get_todos", tags=["todo"])
async def get_todos() -> dict:
    return {"data" : todos}

@app.post("/add_todo", tags=["todo"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data" : "todo added successfully!"
    }

@app.put("/update_todo{id}", tags=["todo"])
async def update_todo(id: int, task: str) -> dict:    
    for todo in todos:
        if int(todo["id"]) == id:
            todo["task"] = task
            return {
                "data" : f"todo with id {id} updated successfully!"
            }

    return {
        "data" : f"todo with id {id} not found!"
    }
    
@app.delete("/delete_todo{id}", tags=["todo"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data" : f"todo with id {id} deleted successfully!"
            }

    return {
        "data" : f"todo with id {id} not found!"
    }
