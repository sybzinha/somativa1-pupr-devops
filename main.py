"""API de gerenciamento de produtos utilizando FastAPI."""

from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# Product model
# pylint: disable=too-few-public-methods
class Product(BaseModel):
    """Modelo de produto contendo ID, nome, preço e quantidade."""
    id: int
    name: str
    price: float
    description: Optional[str] = None

# Sample data
products = [
    Product(id=1, name="Monster Energy", price=7.50, description="Energy drink"),
    Product(id=2, name="Yakult", price=5.00, description=""),
    Product(id=3, name="Pizza", price=30.00, description="Pepperoni pizza"),
    Product(id=4, name="Nuggets", price=15.00, description="Chicken nuggets"),
    Product(id=5, name="Doritos", price=6.00, description=""),
    Product(id=6, name="Coca-Cola", price=5.00, description="Cola soft drink"),
    Product(id=7, name="Açaí", price=10.00, description=""),
    Product(id=8, name="Chocolate", price=4.00, description=""),
]

# Get all products
@app.get("/products", response_model=List[Product])
async def get_products():
    """Retorna todos os produtos cadastrados."""
    return products

# Get a product by ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    """Retorna um produto específico pelo seu ID."""
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Search products by name
@app.get("/products/search", response_model=List[Product])
async def search_products(name: Optional[str] = None):
    """Busca produtos pelo nome."""
    if name is None:
        return products
    filtered = [p for p in products if name.lower() in p.name.lower()]
    return filtered

# Add a new product
@app.post("/products", response_model=Product)
async def create_product(product: Product):
    """Cria um novo produto se o ID ainda não existir."""
    if any(p.id == product.id for p in products):
        raise HTTPException(status_code=400, detail="Product ID already exists")
    products.append(product)
    return product

# Update a product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    """Atualiza um produto existente pelo ID."""
    index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Product not found")
    products[index] = product
    return product

# Delete a product
@app.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    """Remove um produto pelo ID."""
    index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    if index is None:
        raise HTTPException(status_code=404, detail="Product not found")
    deleted_product = products.pop(index)
    return deleted_product
