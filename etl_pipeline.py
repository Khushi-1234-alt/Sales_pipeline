import pandas as pd
from sqlalchemy import create_engine

# -------------------------------------------
# STEP 1: Connect to PostgreSQL
# -------------------------------------------
engine = create_engine("postgresql+psycopg2://postgres:admin123@localhost:5432/sales_db")

# -------------------------------------------
# STEP 2: Load Data
# -------------------------------------------
file_path = "sales_data.csv"
df = pd.read_csv(file_path, encoding='latin1')
print("📥 Raw data loaded:", df.shape)

# -------------------------------------------
# STEP 3: Data Cleaning
# -------------------------------------------
df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'UnitPrice'], inplace=True)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
df.drop_duplicates(inplace=True)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df = df.dropna(subset=['InvoiceDate'])
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
df['total_price'] = df['quantity'] * df['unitprice']

print("✅ Cleaned data shape:", df.shape)
print("🧹 Sample cleaned data:\n", df.head())

# -------------------------------------------
# STEP 4: Load Cleaned Data to PostgreSQL
# -------------------------------------------
df.to_sql('sales_data', engine, if_exists='replace', index=False)
print("🚀 Cleaned data loaded into PostgreSQL successfully!")

# -------------------------------------------
# STEP 5: Create Dimensional Tables (Star Schema)
# -------------------------------------------
# Unique Products
products = df[['stockcode', 'description']].drop_duplicates().reset_index(drop=True)
products['product_id'] = products.index + 1
products = products[['product_id', 'stockcode', 'description']]
products.to_sql('dim_product', engine, if_exists='replace', index=False)

# Unique Customers
customers = df[['customerid', 'country']].drop_duplicates().reset_index(drop=True)
customers['customer_id'] = customers.index + 1
customers = customers[['customer_id', 'customerid', 'country']]
customers.to_sql('dim_customer', engine, if_exists='replace', index=False)

# Fact Table
fact_df = df.merge(products, on=['stockcode', 'description'], how='left') \
            .merge(customers, on=['customerid', 'country'], how='left')

fact_df = fact_df[['invoiceno', 'product_id', 'customer_id', 'quantity', 'unitprice', 'total_price', 'invoicedate']]
fact_df.columns = ['invoice_no', 'product_id', 'customer_id', 'quantity', 'unit_price', 'total_price', 'order_date']

fact_df.to_sql('fact_sales', engine, if_exists='replace', index=False)

print("✅ Data successfully loaded into dimensional model tables (fact + dims)!")
