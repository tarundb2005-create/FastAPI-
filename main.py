from fastapi import FastAPI
from model import Product



app = FastAPI()

products = [
    Product(id = 1, name = "Phone", description = "Flagship",price =  399 , quantity =  1),
    Product(id = 2, name = "Laptop", description = "Apple",price =  1299 , quantity =  1)
]

@app.get('/')
def greet():
    return "Akash Potta"

@app.get('/Products')
def get_products():
    return products

@app.get('/Product/{id}')
def get_product_by_id(id:int):
    return products[id-1]