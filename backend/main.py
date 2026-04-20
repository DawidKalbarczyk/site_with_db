from fastapi import FastAPI

backend = FastAPI()

@backend.get("/")
async def read_root():
    return {"Hello": "World"}

@backend.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}