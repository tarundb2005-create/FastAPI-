from fastapi import FastAPI
from model import Product



app = FastAPI()

products = [
    Product(id = 1, name = "Phone", description = "Flagship",price =  399 , quantity =  1),
    Product(id = 2, name = "Laptop", description = "Apple",price =  1299 , quantity =  1),
    Product(id = 5, name = "PlayStation", description = "Sony",price =  799 , quantity =  1)
]

@app.get('/')
def greet():
    return "Akash Potta"

@app.get('/Products')
def get_products():
    return products

@app.get('/Product/{id}')
def get_product_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "Product is Not Found"

@app.post('/product')
def add_product(product:Product):
    products.append(product)
    return product