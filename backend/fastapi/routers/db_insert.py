from fastapi import APIRouter
from sqlalchemy import create_engine, text
router_insert = APIRouter()

from backend.fastapi.settings import db_name, db_user, db_password

def connect_db(db_name, db_user, db_password):
    return(create_engine(f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"))


@router_insert.post("/insert")
def insert_data():
    engine = connect_db(db_name, db_user, db_password)
    with engine.connect() as connection:
        connection.execute(text("INSERT INTO users (first_name) VALUES ('Emily')"))
    return {"message": "Data inserted successfully"}