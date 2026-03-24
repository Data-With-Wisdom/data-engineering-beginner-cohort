Here's **one simple, beginner-friendly project** you can give to your current Cohort 1 students (and they can showcase on GitHub).

### Project Name:  
**Sales Data ETL Pipeline with Orchestration**  
(End-to-End: Extract → Transform → Load + Simple Scheduling)

- they should create github account

### Tech Stack (All beginner-level):
- **Python** + **Pandas** (for transformation)
- **CSV** file (source data)
- **PostgreSQL** (destination database)
- **Prefect** (for orchestration — very easy, no Docker needed)

### Project Goal:
Students build a complete small ETL pipeline that:
1. Reads raw sales data from a CSV file
2. Cleans and transforms it with Pandas
3. Loads the clean data into a PostgreSQL table
4. Orchestrates the whole process with Prefect (so it can be scheduled or rerun easily)

This looks professional on GitHub and is realistic for junior data engineer / data analyst roles.

### Step-by-Step for Students (You can share this structure):

1. **Setup**  
   - Install: `pip install pandas psycopg2-binary prefect sqlalchemy`  
   - Create a free PostgreSQL database (use Supabase, Neon, or local Postgres)  
   - Download or create a sample `sales_data.csv` (columns: order_id, date, customer_id, product, quantity, price, region)

2. **Extract**  
   - Read CSV using Pandas

3. **Transform** (with Pandas)  
   - Clean data (handle missing values, remove duplicates)  
   - Create new columns (e.g., `total_amount = quantity * price`, `year_month` from date)  
   - Filter or aggregate if needed (e.g., sales by region)

4. **Load**  
   - Use SQLAlchemy or psycopg2 to insert the cleaned DataFrame into a Postgres table (`sales_cleaned`)

5. **Orchestrate with Prefect** (the simple part)  
   ```python
   from prefect import flow, task
   import pandas as pd
   from sqlalchemy import create_engine

   @task
   def extract():
       return pd.read_csv("sales_data.csv")

   @task
   def transform(df):
       # cleaning & transformation code here
       df = df.dropna()
       df['total_amount'] = df['quantity'] * df['price']
       return df

   @task
   def load(df):
       engine = create_engine("postgresql+psycopg2://user:pass@host/dbname")
       df.to_sql("sales_cleaned", engine, if_exists="replace", index=False)

   @flow
   def sales_etl_pipeline():
       df = extract()
       df_clean = transform(df)
       load(df_clean)

   # Run it
   if __name__ == "__main__":
       sales_etl_pipeline()
   ```

6. **Bonus for GitHub**:
   - Add a `README.md` with project description, tech stack, screenshots of the Postgres table, and how to run it.
   - Include requirements.txt and a simple schedule example (`prefect deployment` or just run manually).
