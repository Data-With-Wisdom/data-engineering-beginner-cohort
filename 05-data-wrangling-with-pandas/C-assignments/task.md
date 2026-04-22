## Take-Home Assignment 1

Customer Data Cleaning & Analysis (File-based)

**Task**  
Using the dataset (`assignments-datasets/customers.csv`), write a script that:
1. Loads the CSV
2. Inspects the data (`head`, `info`, `isnull`)
3. Cleans it (fix missing values + wrong data types)
4. Creates a new column `Spend_Category`:
   - "Low" if Spend < 100
   - "Medium" if 100 <= Spend <= 200
   - "High" if Spend > 200
5. Finds average spend per city
6. Sorts by highest spend
7. Exports: `assignment-datasets/clean_output_customers.csv`

**Dataset path:** `05-data-wrangling-with-pandas/datasets/assignments-datasets/customers.csv`

---

## Assignment 2

**Objective**  
Build a complete basic ETL pipeline where you:
- Create and populate a raw table using **pure SQL** (as taught in earlier weeks).
- Extract the data into Pandas.
- Clean and transform it.
- Load the cleaned data into a new PostgreSQL table.

**Instructions**

### Step 1: SQL Setup (Do this first in pgAdmin)

1. Create a new database (optional but recommended for practice):
   ```sql
   CREATE DATABASE etl_practice;
   ```

2. Connect to the new (or your existing) database and run the following statements:

   ```sql
   -- Create the raw table
   CREATE TABLE IF NOT EXISTS raw_orders (
       OrderID INTEGER PRIMARY KEY,
       CustomerID INTEGER,
       OrderDate TEXT,
       Amount TEXT,
       Status TEXT
   );

   -- Insert messy raw data
   INSERT INTO raw_orders (OrderID, CustomerID, OrderDate, Amount, Status) VALUES
   (101, 1, '2024-02-01', '99.99', 'Completed'),
   (102, 2, NULL, '150.5', 'Pending'),
   (103, 3, '2024-02-03', 'abc', 'Completed'),
   (104, 1, '2024-02-04', '200', NULL),
   (105, 4, '2024-02-05', '75.25', 'Completed')
   ON CONFLICT (OrderID) DO NOTHING;

   -- Verify the data
   SELECT * FROM raw_orders;
   ```

### Step 2: Python ETL Script

Create a file called `etl_assignment2.py` and write a script that does the following:

1. **Extract**: Connect to PostgreSQL and read the `raw_orders` table into a Pandas DataFrame using `pd.read_sql()`.

2. **Transform**:
   - Convert `OrderDate` to proper datetime (handle invalid/missing values).
   - Convert `Amount` to numeric (handle non-numeric values like 'abc').
   - Fill missing values reasonably (e.g., Status -> 'Unknown', Amount -> mean or 0, OrderDate -> a default date).
   - Create a new column `Order_Year` extracted from `OrderDate`.
   - Create a new column `Revenue_Category`:
     - "Low" if Amount < 100
     - "Medium" if 100 <= Amount <= 200
     - "High" if Amount > 200

3. **Load**: Write the cleaned DataFrame to a new table called `clean_orders` using `df.to_sql(...)`.

**Requirements for the script**
- Use SQLAlchemy `create_engine` for the connection.
- Use `if_exists="replace"` when writing to `clean_orders` (good for repeated runs).
- Include clear comments for each section: `# EXTRACT`, `# TRANSFORM`, `# LOAD`.
- Print messages like "ETL completed successfully!" at the end.
- Handle the connection properly (you can close it or let the engine manage it).


**Expected Cleaned Output (for reference - do not hardcode!)**  
Students should end up with a table that has proper data types, no obvious errors, and the two new columns.
