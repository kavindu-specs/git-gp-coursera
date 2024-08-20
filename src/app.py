from database import get_db, startup_event
from fastapi import FastAPI
from models import Item
app = FastAPI()
app.add_event_handler("startup", startup_event)

#get items api
@app.get("/items/")
def create_item(item:Item):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * from db" )
    conn.commit()
    item.id = cursor.lastrowid
    return item

@app.post("/items/")
def create_item(item:Item):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, price, is_offer) VALUES (?, ?, ?)", (item.name, item.price, int(item.is_offer) if item.is_offer else None), )
    conn.commit()
    item.id = cursor.lastrowid
    return item
