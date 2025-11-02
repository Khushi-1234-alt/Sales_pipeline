import pandas as pd
from sqlalchemy import create_engine

# Step 1: Create the database connection
engine = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5432/sales_db")

# Step 2: Create some dummy sales data
data = {
    "product_name": ["Laptop", "Phone", "Tablet"],
    "category": ["Electronics", "Electronics", "Electronics"],
    "quantity": [3, 5, 2],
    "unit_price": [60000, 20000, 15000],
    "total_price": [180000, 100000, 30000],
    "order_date": ["2025-11-02", "2025-11-01", "2025-10-30"],
    "region": ["North", "South", "East"]
}

df = pd.DataFrame(data)

# Step 3: Insert data into PostgreSQL
df.to_sql('sales_data', engine, if_exists='append', index=False)

print("✅ Data inserted successfully!")
