# 📘 Week 3: SQL Foundations

---

## 🔹 Lesson 3.2 — Database Fundamentals

### What is a Database?

A **database** is an organized collection of data stored electronically. Instead of saving data in random files, a database stores it in a structured way so you can easily search, update, and retrieve it.

**Real-life example:** Think of your phone contacts. All names, numbers, and emails are stored in an organized way — that's a simple database.

---

### Types of Databases: Relational vs Non-Relational

| Feature | Relational (SQL) | Non-Relational (NoSQL) |
|--------|-----------------|----------------------|
| Structure | Tables (rows & columns) | Documents, key-value, graphs |
| Language | SQL | Varies (JSON, etc.) |
| Examples | PostgreSQL, MySQL | MongoDB, Redis |
| Best for | Structured, consistent data | Flexible or unstructured data |

> 💡 As a **data analyst**, you'll mostly work with **relational databases**.

---

### What is a Relational Database?

A **relational database** stores data in **tables** that are **linked (related) to each other**.

**Example:** A `customers` table and an `orders` table can be related — every order belongs to a customer.

---

### What is an RDBMS?

**RDBMS** = **Relational Database Management System**

It's the software that manages your relational database. It lets you create databases, run SQL queries, and manage your data safely.

**Examples of RDBMS:**
- PostgreSQL ✅ *(what we use in this course)*
- MySQL
- SQLite
- Microsoft SQL Server

---

### What is a Database Engine?

A **database engine** is the core part of the RDBMS that actually **reads, writes, and processes** your data. You don't interact with it directly — it works behind the scenes when you run a SQL query.

---

### What is a Table?

A **table** is where data lives in a relational database. It looks just like a spreadsheet — with **rows** and **columns**.

**Example — `employees` table:**

| employee_id | name    | department | salary |
|-------------|---------|------------|--------|
| 1           | Ada     | Finance    | 80000  |
| 2           | Chidi   | Marketing  | 65000  |
| 3           | Ngozi   | Finance    | 72000  |

---

### Rows vs Columns

- A **column** = a **field** or **attribute** (e.g., `name`, `salary`) — it defines what type of data is stored
- A **row** = a **record** (e.g., one employee's full details) — it's one entry in the table

> Think of columns as questions ("What's the name?") and rows as answers ("Ada, Chidi, Ngozi").

---

### What is a Primary Key?

A **Primary Key** is a column that **uniquely identifies each row** in a table. No two rows can have the same primary key value, and it can never be empty.

In our example above, `employee_id` is the primary key — every employee has a unique ID.

---

### How Relational Data is Structured

In relational databases, tables are connected through **keys**. One table can reference another using a **Foreign Key** — a column that points to the primary key of another table.

**Example:**

`orders` table has a `customer_id` column → this references `customers.customer_id`

This relationship is what makes the database **relational**.

---

## 🔹 Lesson 3.4 — Data Types, CREATE DATABASE, CREATE TABLE, DROP TABLE

### Common Data Types in PostgreSQL

| Data Type | What it stores | Example |
|-----------|----------------|---------|
| `INT` | Whole numbers | `25`, `1000` |
| `DECIMAL` / `NUMERIC` | Numbers with decimals | `99.99` |
| `VARCHAR(n)` | Text up to n characters | `'Ada'` |
| `TEXT` | Unlimited text | Long descriptions |
| `DATE` | Date only | `'2024-01-15'` |
| `BOOLEAN` | True or False | `TRUE`, `FALSE` |

---

### CREATE DATABASE

```sql
CREATE DATABASE sales_db;
```

This creates a new empty database called `sales_db`.

---

### CREATE TABLE

```sql
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY,
    name          VARCHAR(100),
    email         VARCHAR(150),
    city          VARCHAR(50),
    signup_date   DATE
);
```

**What this does:**
- Creates a table called `customers`
- Defines 5 columns with their data types
- Sets `customer_id` as the primary key

---

### DROP TABLE

```sql
DROP TABLE customers;
```

> ⚠️ **Warning:** This permanently deletes the table and ALL its data. Use with caution!

---

## 🔹 Lesson 3.5 — SELECT, WHERE, ORDER BY, LIMIT

These are the most common SQL commands you'll use every single day.

---

### SELECT — Retrieve Data

```sql
-- Get everything from the table
SELECT * FROM customers;

-- Get only specific columns
SELECT name, city FROM customers;
```

`*` means "all columns". Be specific when you can — it's faster and cleaner.

---

### WHERE — Filter Rows

```sql
-- Only customers from Lagos
SELECT * FROM customers
WHERE city = 'Lagos';

-- Only customers who signed up after 2023
SELECT * FROM customers
WHERE signup_date > '2023-01-01';
```

The `WHERE` clause tells SQL **which rows** to return.

---

### ORDER BY — Sort Results

```sql
-- Sort by name A to Z
SELECT * FROM customers
ORDER BY name ASC;

-- Sort by signup date, newest first
SELECT * FROM customers
ORDER BY signup_date DESC;
```

- `ASC` = Ascending (A→Z, 1→10) ← default
- `DESC` = Descending (Z→A, 10→1)

---

### LIMIT — Control How Many Rows You Get

```sql
-- Only show the first 5 rows
SELECT * FROM customers
LIMIT 5;
```

> 💡 Always use `LIMIT` when exploring a new table — it prevents accidentally loading millions of rows.

---

### Putting It All Together

```sql
SELECT name, city, signup_date
FROM customers
WHERE city = 'Lagos'
ORDER BY signup_date DESC
LIMIT 10;
```

**In plain English:** *"Show me the name, city, and signup date of customers from Lagos, ordered from newest to oldest, but only the top 10."*

---

## 🔹 Lesson 3.6 — Filtering: AND / OR / IN

### AND — All conditions must be true

```sql
SELECT * FROM customers
WHERE city = 'Lagos'
AND signup_date > '2023-01-01';
```

Returns customers who are **both** from Lagos **and** signed up after 2023.

---

### OR — At least one condition must be true

```sql
SELECT * FROM customers
WHERE city = 'Lagos'
OR city = 'Abuja';
```

Returns customers from Lagos **or** Abuja (or both).

---

### IN — Match any value in a list

```sql
SELECT * FROM customers
WHERE city IN ('Lagos', 'Abuja', 'Kano');
```

This is a cleaner way to write multiple `OR` conditions. Same result, less code.

---

### Combining Filters

```sql
SELECT * FROM customers
WHERE city IN ('Lagos', 'Abuja')
AND signup_date > '2023-01-01';
```

> 💡 Use parentheses when mixing `AND` and `OR` to avoid confusion:
> ```sql
> WHERE (city = 'Lagos' OR city = 'Abuja') AND signup_date > '2023-01-01'
> ```

---

## 🔹 Lesson 3.7 — Aggregations: COUNT, SUM, AVG

Aggregation functions **summarize** your data. Instead of seeing every row, you get one result.

---

### COUNT — How many rows?

```sql
-- How many customers do we have?
SELECT COUNT(*) FROM customers;

-- How many customers are from Lagos?
SELECT COUNT(*) FROM customers
WHERE city = 'Lagos';
```

---

### SUM — Add up values

```sql
-- Total revenue from all orders
SELECT SUM(amount) FROM orders;
```

---

### AVG — Calculate the average

```sql
-- Average order amount
SELECT AVG(amount) FROM orders;
```

---

### Other useful ones

```sql
SELECT MAX(amount) FROM orders;  -- Highest order
SELECT MIN(amount) FROM orders;  -- Lowest order
```

---

## 🔹 Lesson 3.8 — GROUP BY

`GROUP BY` lets you aggregate data **by category**. Instead of one total, you get totals *per group*.

### Example

```sql
-- How many customers are in each city?
SELECT city, COUNT(*) AS total_customers
FROM customers
GROUP BY city;
```

**Result:**

| city   | total_customers |
|--------|----------------|
| Lagos  | 120            |
| Abuja  | 85             |
| Kano   | 43             |

---

### Another Example

```sql
-- Total sales per product
SELECT product_name, SUM(amount) AS total_sales
FROM orders
GROUP BY product_name
ORDER BY total_sales DESC;
```

> 💡 **Rule to remember:** Any column in your `SELECT` that is **not** inside an aggregation function **must** be in the `GROUP BY`.

---

## 🔹 Lesson 3.9 — Creating a Related Table

Now let's create a second table that relates to `customers`. This shows how relational databases work in practice.

```sql
-- First, we already have:
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY,
    name          VARCHAR(100),
    city          VARCHAR(50)
);

-- Now create a related orders table
CREATE TABLE orders (
    order_id      INT PRIMARY KEY,
    customer_id   INT,           -- This links to the customers table
    product_name  VARCHAR(100),
    amount        DECIMAL(10, 2),
    order_date    DATE
);
```

The `customer_id` column in `orders` is a **Foreign Key** — it references the `customer_id` in `customers`.

This connection allows you to ask questions like: *"Show me all orders placed by customers from Lagos."*

---

## 🔹 Lesson 3.10 — INNER JOIN and LEFT JOIN

Joins allow you to **combine data from two tables** into one result.

---

### INNER JOIN — Only matching rows from both tables

```sql
SELECT c.name, o.product_name, o.amount
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id;
```

**What this returns:** Only customers who **have** placed an order. Customers with no orders are excluded.

---

### LEFT JOIN — All rows from the left table, even if no match

```sql
SELECT c.name, o.product_name, o.amount
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;
```

**What this returns:** All customers — even those who haven't placed an order. For customers with no orders, the order columns will show `NULL`.

---

### Visual Comparison

```
customers table:    orders table:
Ada   (id=1)        id=1 → Ada's order
Chidi (id=2)        id=1 → Ada's second order
Ngozi (id=3)        (no orders for Chidi or Ngozi)

INNER JOIN result:        LEFT JOIN result:
Ada   → order 1           Ada   → order 1
Ada   → order 2           Ada   → order 2
                          Chidi → NULL
                          Ngozi → NULL
```

> 💡 Use **INNER JOIN** when you only care about records that exist in both tables. Use **LEFT JOIN** when you want to keep all records from the first (left) table regardless.

---

### Using Aliases for Cleaner Queries

`c` and `o` are **aliases** — short names for the tables. This makes queries much easier to read, especially when joining multiple tables.

---


## 🔹 Week 3 Assignment

**Answer 5 Real Business Questions Using SQL**

Using the `customers` and `orders` tables, write SQL queries to answer these questions — then explain each in plain English.

---

**Question 1:** How many customers do we have in total?

**Question 2:** Which city has the most customers?

**Question 3:** What is the total revenue generated from all orders?

**Question 4:** Who are the top 5 customers by total amount spent?

**Question 5:** How many customers have never placed an order?

---

### Submission Format

For each question, provide:

1. Your **SQL query**
2. A **plain English explanation** of what the query does

---

### Example Submission (for guidance)

**Question:** What is the total revenue from orders placed by Lagos customers?

**SQL:**
```sql
SELECT SUM(o.amount) AS total_revenue
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Lagos';
```

**Explanation:** This query joins the orders and customers tables, filters for Lagos customers only, and adds up all their order amounts.

**Interpretation:** Lagos customers generated ₦4.5M in total revenue, making it our highest-performing city.

---

> 🎯 **Key Mindset Reminder:**
> SQL is not about memorizing syntax. It's about asking the right questions and letting the data tell you the story.