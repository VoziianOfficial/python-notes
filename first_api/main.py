from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class ProductCreate(BaseModel):
    name: str
    price: float


@app.get("/")
def home():
    return {"message": "Hello from my first API"}


products = [
    {"id": 1, "name": "T-shirt", "price": 299},
    {"id": 2, "name": "Sneakers", "price": 799},
    {"id": 3, "name": "Bag", "price": 499},
]


# get
@app.get("/products")
def get_products():
    return products


# filter
@app.get("/products/filter")
def filter_products(max_price: float):
    result = []
    for product in products:
        if product["price"] <= max_price:
            result.append(product)

    return result


# filter second
@app.get("/products/filter")
def filter_products(max_price: float = None, name: str = None):
    result = []

    for product in products:
        if max_price is not None and product["price"] > max_price:
            continue

        if name is not None and name.lower() not in product["name"].lower():
            continue

        result.append(product)

    return result


# get id
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


# post
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price,
    }

    products.append(new_product)

    return new_product


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None


# patch
@app.patch("/products/{product_id}")
def update_product(product_id: int, product_data: ProductUpdate):
    for product in products:
        if product["id"] == product_id:
            if product_data.name is not None:
                product["name"] = product_data.name

            if product_data.price is not None:
                product["price"] = product_data.price

            return product

    raise HTTPException(status_code=404, detail="Product not found")


# put
class ProductReplace(BaseModel):
    name: str
    price: float


@app.put("/products/{product_id}")
def replace_product(product_id: int, product_data: ProductReplace):
    for product in products:
        if product["id"] == product_id:
            product["name"] = product_data.name
            product["price"] = product_data.price
            return product

    raise HTTPException(status_code=404, detail="Product not found")


# delete
@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return {"message": "Product deleted"}

    raise HTTPException(status_code=404, detail="Product not found")
