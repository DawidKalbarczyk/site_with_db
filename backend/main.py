from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routers.static_content import router
from app.routers.db_insert import router_insert
from app.routers.dynamic_content import router_get_users

backend = FastAPI(title="Backend DB API", version="1.0.0")

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


backend.include_router(router, prefix="/backend")
backend.include_router(router_insert, prefix="/backend")
backend.include_router(router_get_users, prefix="/backend")
