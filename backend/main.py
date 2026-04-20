from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

backend = FastAPI()

backend.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@backend.get("/")
async def read_root():
    return {"Hello": "World"}

@backend.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


