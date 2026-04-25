from fastapi import APIRouter
from sqlalchemy import create_engine, text
router_get = APIRouter()

from backend.settings import db_name, db_user, db_password

def connect_db(db_name, db_user, db_password):
    return(create_engine(f"postgresql://{db_user}:{db_password}@db:5432/{db_name}"))

