from fastapi import FastAPI;
app = FastAPI()

# minimal app get request
@app.get("/", tags=['ROOT'] )
async def root() -> dict:
    return{"ping":"pong"}

#Get == read a todo
@app.get("/todo", tags=['todos'])
async def get_todo() -> dict:
    return{"data": todos}

#Post == Create a todo
@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data": "You have sucessfully added a todo"
        }
#Put == update a todo
@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Activity'] == body['Activity']
            return {
                "data": f"Todo with id{id} has been updated !"
            }
        return {
            "data": f"Todo with the id number {id } was not found !"
        }


#Delete === Delete a todo
@app.delete("/todo/{id}", tags =['todos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todos.remove(todo)
            return{
                "data": f" Todo with id number {id } is deleted successfully"
            }
        return{
            "data": f"The todo with this id  {id} does not exist!"
        }
            




todos =[
    {"id":"1",
     "Activity": " code 4 hours everyday"
     },
    { "id":"2",
     "Activity": " jog 1 hour every evening"
     },
     { "id":"3",
     "Activity": " drink a glass of water every hour"
     }
]