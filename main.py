from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# * #############################################################
# * #                       GET method                          #
# * #############################################################
# @app.get("/")
# async def home():
#     return {
#         "Message":"Welcome to the FastAPI application!"
#     }

# #* create the userlist
# @app.get("/users")
# async def userList():
#     return{
#         "users": [
#             {"id": 1, "name": "John Doe"},
#             {"id": 2, "name": "Jane Smith"},
#             {"id": 3, "name": "Alice Johnson"}
#         ]
#     }

# #* create the contact route with query parameter (default value of name is 'null')
# @app.get("/contact")
# async def get_contact(name: str = 'null'):
#     return {
#         "Name":name
#     }

# #* create the products route with query parameter (default value of limit is 10)
# @app.get("/products")
# async def get_products(limit: int = 10):
#     return {
#         "limit": limit
#     }


# * #############################################################
# * #      Default parameter & Optional parameter               #
# * #############################################################
# @app.get("/items")
# async def get_items(name: str = None, price: int = 10):
#     return {
#         "name": name,
#         "price": price
#     }

# * #############################################################
# * #                POST API Method                            #
# * #############################################################
# class User(BaseModel):
#     age: int
#     name: str
#     email: str

# @app.post("/create_user")
# async def create_user(user: User):
#     return{
#         "Message":"User created successfully!",
#         "status": 200,
#         "user":user
#     }

# * #############################################################
# * #                Pydantic Model                             #
# * #############################################################

# class UserAddress(BaseModel):
#     city: str
#     pincode: int

# class User(BaseModel):
#     name: str
#     age: int
#     email: str
#     address: UserAddress

# @app.post("/create_user")
# async def create_user(user: User):
#     return {
#         "message": "User create successfull",
#         "status": 200,
#         "user-info": user.model_dump()
#     }

# * #############################################################
# * #                         Todo API                          #
# * #############################################################

# todos = []

# class Todo(BaseModel):
#     id: int
#     title: str
#     description: str
#     completed: bool


# # * Create a todo
# @app.post("/todos")
# async def create_todo(todo: Todo):
#         todos.append(todo)
#         return{
#               "message": "Todo created successfully",
#               "status": 200,
#               "data":todo
#         }


# # * Get all todos
# @app.get("/get_todos")
# async def get_todos():
#     return {
#         "message": "Todos fetched successfully",
#         "status": 200,
#         "data": todos
#     }


# # * using path parameter to get a specific todo by id
# @app.get("/get_todos/{todo_id}")
# async def get_todos(todo_id: int):
#     for todo in todos:
#         if todo.id == todo_id:
#              return todo    
#     return {
#         "message": "Todo not found",
#         "status": 404,
#         "data": None
#     }

# # * Update a todo by id
# @app.put("/update_todo/{todo_id}")
# async def update_todo(todo_id: int, updated_todo: Todo):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             todos[index] = updated_todo
#             return {
#                 "message": "Todo updated successfully",
#                 "status": 200,
#                 "data": updated_todo
#             }
#     return {
#         "message": "Todo not found",
#         "status": 404,
#         "data": None
#     }


# # * Delete a todo by id
# @app.delete("/delete_todo/{todo_id}")
# async def delete_todo(todo_id: int):
#     for index, todo in enumerate(todos):
#         if todo.id == todo_id:
#             deleted_todo = todos.pop(index)
#             return {
#                 "message": "Todo deleted successfully",
#                 "status": 200,
#                 "data": deleted_todo
#             }
#     return {
#         "message": "Todo not found",
#         "status": 404,
#         "data": None
#     }


# * #############################################################
# * #                Path + Query + Body Combo                  #
# * #############################################################

users = []

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
async def create_user(user:User):
    users.append(user)
    return {
        "data":user
    }

@app.put("/users/{user_id}")
async def updated_user(user_id: int, user:User, notify:bool = False):
    if user_id < len(users):
        users[user_id] = user

        return {
            "message": "User Update",
            "notify":notify,
            "data":user            
        }