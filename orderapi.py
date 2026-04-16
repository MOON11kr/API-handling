from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

orders = []

class OrderData(BaseModel):
    item_name: str

@app.post("/order")
def place_order(order_from_user: OrderData):
    orders.append(order_from_user.item_name)
    
    return {
        "message": "Order placed",
        "orders": orders
    }

@app.get("/orders")
def get_orders():
    return {
        "orders": orders
    }