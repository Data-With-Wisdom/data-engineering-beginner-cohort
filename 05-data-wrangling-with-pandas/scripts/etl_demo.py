import pandas as pd
from sqlalchemy import create_engine

print("=== STARTING PANDAS ETL PIPELINE ===\n")

# ====================== EXTRACT ======================
print("1. EXTRACT: Loading raw data from CSV...")
df = pd.read_csv("sales_data.csv")
print(df)

# ====================== TRANSFORM ======================
print("\n2. TRANSFORM: Cleaning and enriching the data...")

# Fix wrong data types
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

# Handle missing values (basic imputation for demo)
df["Order_Date"] = df["Order_Date"].fillna(pd.Timestamp("2024-01-01"))
df["Quantity"] = df["Quantity"].fillna(1)
df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].mean())

# Create new calculated column
df["Total_Amount"] = df["Quantity"] * df["Unit_Price"]

print("Cleaned & transformed data:")
print(df)

# ====================== LOAD ======================
print("\n3. LOAD: Writing cleaned data to PostgreSQL...")

# Update these credentials with your own
engine = create_engine(
    "postgresql+psycopg2://your_username:your_password@localhost:5432/your_database"
)

df.to_sql("clean_sales", engine, if_exists="replace", index=False)

print("✅ ETL FINISHED! Data is now in PostgreSQL table 'clean_sales'")
print("You can query it with: SELECT * FROM clean_sales;")