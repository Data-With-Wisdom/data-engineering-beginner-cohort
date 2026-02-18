# 7-Week Course Structure (Adjusted & Realistic)

---

### **Pre-Course Setup**
*Goal: Remove technical barriers early*
- **Environment Setup Guide**
  - Installing Python, VS Code, Jupyter
  - Creating accounts: GitHub
  - Testing installations with a "Hello World" script
- **Welcome Pack**
  - Course expectations & time commitment (realistic: 2 - 4 hrs/week)

---

## 🔹 Week 1: What is Data Engineering?
*Focus: Building intuition before diving in*

**Core Content:**
- What Data Engineering actually is (use relatable examples: Netflix recommendations, food delivery apps)
- **Day in the life**: What DEs actually do vs what beginners think they do
- Roles in data teams:
  - Data Engineer vs Data Analyst vs Data Scientist vs Analytics Engineer
  - **Mini activity**: Match job descriptions to roles
- How data flows in companies:
  - Source → Storage → Processing → Consumption (simple diagram)
  - Real-world examples (e.g., e-commerce order tracking)
- Batch vs Streaming (high-level, with everyday analogies)
- **Types of companies that hire DEs** (tech, finance, healthcare, e-commerce)
- **What makes a good Data Engineer** (problem-solving > tool knowledge)
- **Career pathways** (junior → mid → senior progression)
- **Assignment**: Write a 1-page reflection: "What does data engineering mean to me?"


---

## 🔹 Week 2: The Language of Data Engineering (Concepts & Mental Models)

**Focus:** Thinking like a data engineer before tools

**Core Content:**
- Data lifecycle (generation → collection → storage → processing → analysis → archival)
- **ETL vs ELT vs Zero-ETL** (with visual diagrams)
- Data types:
  - Structured (databases), Semi-structured (JSON), Unstructured (images, text)
  - **Activity**: Identify data types in real-world scenarios
- Storage systems:
  - Data Warehouses vs Data Lakes vs Lakehouses (when to use what)
  - **Simple comparison table**
- Data modeling basics:
  - Tables, primary/foreign keys
  - Facts vs Dimensions (with e-commerce example)
- Data quality, validation, freshness (why this matters)
- Pipelines & orchestration (conceptual only)
- **Common data formats**: CSV, JSON, Parquet, Avro (what they look like)
- **Data engineering mistakes beginners make** (and how to avoid them)

### Assignment:

* Draw and explain a **simple data flow diagram** for a real business

👉 This week makes *everything else make sense*.

---

## 🔹 Week 3: SQL Foundations (One Week, Properly Scoped)

**Key mindset:**

> “SQL is not everything — but without SQL, nothing else matters.”

### What you teach (ONLY essentials):

* Setup RDBMS PostgreSQL
* What is SQL and Types of SQL
* SELECT, WHERE, ORDER BY, LIMIT
* Filtering (AND / OR / IN)
* Aggregations (COUNT, SUM, AVG)
* GROUP BY
* INNER & LEFT JOIN (only these two)
* Reading query results like a story

❌ What you **do NOT** deep dive:

* Complex subqueries
* Advanced window functions

(Those are **mentioned**, not mastered.)

### Assignment:

* Answer **5 real business questions** using SQL
* Explain queries in plain English

---

## 🔹 Week 4: Python Essentials for Data Engineers

**Focus:** Python as a *tool*, not a programming course

### What you teach:

**Core Content:**
- What is Python
- **Virtual environments** (venv basics - keeping projects clean)
- Python basics: variables, data types, loops, conditionals
- Functions: writing reusable code
- **Data structures**: lists, dictionaries, tuples (with data examples)
- Reading/writing files: CSV, JSON
- String manipulation (cleaning messy data)
- Error handling: try/except basics
- **Why Python for data engineering?** (vs other languages)
- **Code organization**: Writing readable scripts (naming, comments)
- **Debugging tips** (print statements, reading error messages)
- **Practice problems**: 10 short coding exercises
- **Assignment**: Build a script that reads a CSV, cleans it, and exports cleaned version


❌ Skip:

* OOP
* Classes
* Advanced Python topics

### Assignment:

* Write a Python script that:

  * Reads a CSV
  * Cleans it
  * Saves cleaned output

👉 This week is about **confidence**, not mastery.

---

## 🔹 Week 5: Data Wrangling with Pandas

**This is where things “click” for most students.**

### What you teach:

**Core Content:**
- DataFrames & Series (what they are)
- Loading data: `read_csv()`, `read_json()`
- Inspecting data: `.head()`, `.info()`, `.describe()`
- Cleaning:
  - Handling nulls (`.fillna()`, `.dropna()`)
  - Renaming columns
  - Changing data types
- Transformations:
  - Filtering rows, selecting columns
  - Creating new columns
  - Grouping & aggregating
  - Merging/joining DataFrames
- Exporting: `to_csv()`, `to_excel()`
- **Pandas vs SQL**: When to use which
- **Common Pandas gotchas** (chained indexing, copies vs views)
- **Real-world dirty datasets** (missing values, duplicates, inconsistent formatting)

### Mini-Project:

* Clean a messy HR or sales dataset
* Produce a clean final table

👉 Pandas gets **one focused week**, not scattered.

---

## 🔹 Week 6: Working Like a Professional + Intro to Big Data

This is where you **merge professionalism + big-picture thinking**.

### Part 1: Professional Skills

* Git & GitHub basics
* Repo structure
* README writing
* requirements.txt
* Pushing projects to GitHub
* **Environment files**: requirements.txt, .env basics

### Part 2: Intro to Big Data (Conceptual)

* When data gets “big”
* Why Spark exists
* Why NiFi exists
* Pandas vs Spark (decision framework)
* Overview of Airflow, Kafka
* Intro to cloud platforms
* How companies choose stacks

### Assignment:

* Push previous project to GitHub
* Short write-up: *“When would I need Spark or NiFi?”*

👉 This week answers: **“What’s next after this course?”**

---

## 🔹 Week 7: Capstone Project (End-to-End): Present this to student and explain my code and project
*Goal: Synthesize everything learned*

**Project Requirements:**
- **Dataset**: Realistic messy data (e-commerce orders, event logs, etc.)
- **Tasks**:
  1. Clean and transform data using Pandas
  2. Load into SQLite database
  3. Write 5 SQL queries answering business questions
  4. Create a data pipeline script (automate steps 1-2)
  5. Document everything in GitHub README
- **Deliverables**:
  - GitHub repo with code
  - Written report explaining:
    - Data flow diagram
    - Transformation logic
    - Query explanations
    - Where Spark/NiFi would fit at scale
- **Showcase session** (present to cohort + get feedback)

---

### **Post-Course: What's Next?**
*Goal: Clear path forward*

- **Career Guidance**:
  - How to apply for junior DE roles
  - Resume tips for career changers
  - Portfolio projects that impress
- **Advanced Topics Roadmap**:
  - Next tools to learn (Airflow, dbt, Docker)
  - When to take advanced cohort
- **Continued Learning Resources** (curated list)