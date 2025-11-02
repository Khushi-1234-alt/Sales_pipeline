# db_config.py
from sqlalchemy import create_engine

def get_engine():
    # PostgreSQL connection string
    return create_engine("postgresql+psycopg2://postgres:admin123@localhost:5432/sales_db")
