from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# #* create home route with GET method
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

# # * default parameter & optional parameter
# @app.get("/items")
# async def get_items(name: str = None, price: int = 10):
#     return {
#         "name": name,
#         "price": price
#     }


# class User(BaseModel):
#     age: int
#     name: str
#     email: str

# # * POST API Method
# @app.post("/create_user")
# async def create_user(user: User):
#     return{
#         "Message":"User created successfully!",
#         "status": 200,
#         "user":user
#     }


#* Pydantic Model

class UserAddress(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    email: str
    address: UserAddress

@app.post("/create_user")
async def create_user(user: User):
    return {
        "message": "User create successfull",
        "status": 200,
        "user-info": user.model_dump()
    }