from fastapi import FastAPI, status, Request
from pydantic import BaseModel
import time
import sqlite3


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

# users = []

# class User(BaseModel):
#     name: str
#     age: int

# @app.post("/api/v1/users")
# async def create_user(user:User):
#     users.append(user)
#     return {
#         "data":user
#     }

# @app.put("/api/v1/users/{user_id}")
# async def updated_user(user_id: int, user:User, notify:bool = False):
#     if user_id < len(users):
#         users[user_id] = user

#         return {
#             "message": "User Update",
#             "notify":notify,
#             "data":user            
#         }


# * #############################################################
# * #                    Response Model                         #
# * #############################################################

# class User(BaseModel):
#     name: str
#     age: int
#     password: str

# # * eikhane thik hobe user response e ami ki ki dibo eikhane, that's it    
# class UserResponse(BaseModel):
#     name: str
#     age: int
    
# @app.get("/user", response_model=UserResponse)
# async def get_user():
#     return {
#         "name": "John Doe",
#         "age": 30,
#         "password": "123456"
#         }


# * #############################################################
# * #             Status Code and Response                      #
# * #############################################################

# @app.post("/create_user", status_code= status.HTTP_201_CREATED)
# def create_user():
#     return {
#         "message":"User Create"
#     }
    
# @app.get("/user")
# def get_user():
#     return{
#         "status":"Success",
#         "message":"User Fetched",
#         "data":{
#             "name":"Zobayer",
#             "age":26,
#             "location":"Dhaka, Gopalganj"
#         }
#     }    


# * #############################################################
# * #                          Middleware                       #
# * #############################################################

# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#     print("Request Recived")

#     response = await call_next(request)

#     print("Response Sent")

#     return response


# @app.middleware("http")
# async def log_middleware(request: Request, call_next):
#     start_time = time.time()

#     response = await call_next(request)

#     process_time = time.time()-start_time

#     print(f"Path:{request.url.path} | Time: {process_time}")

#     return response

# * #############################################################
# * #                   Database Integration                    #
# * #############################################################

conn = sqlite3.connect("test.db", check_same_thread=False) # eikhane 2 ta jinis ditei hobe

cursor = conn.cursor()  # curson sql query run kore

cursor.execute("""CREATE TABLE IF NOT EXISTS todos (
id INTEGER PRIMARY KEY,
title TEXT,
completed TEXT
)""")

conn.commit()


@app.get("/")
def home():
    return {
        "message":"SQL Connected Fine"
    }
