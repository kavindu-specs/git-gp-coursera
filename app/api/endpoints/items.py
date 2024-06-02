import sqlite3
from fastapi import APIRouter, Depends
from app.models.items import Item, ItemResponse
from app.core.db import get_db_conn

router = APIRouter()

@router.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(item: Item, conn: sqlite3.Connection = Depends(get_db_conn)):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, price, is_offer) VALUES (?, ?, ?)",
        (item.name, item.price, int(item.is_offer) if item.is_offer else None)
    )
    conn.commit()
    item.id = cursor.lastrowid
    return item

@router.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item, conn: sqlite3.Connection = Depends(get_db_conn)):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name = ?, price = ?, is_offer = ? WHERE id = ?",
        (item.name, item.price, int(item.is_offer) if item.is_offer else None, item_id)
    )
    conn.commit()
    return item

@router.delete("/items/{item_id}")
def delete_item(item_id: int, conn: sqlite3.Connection = Depends(get_db_conn)):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    return {"message": "Item deleted"}