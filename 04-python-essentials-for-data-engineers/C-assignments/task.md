## 📘 Data Engineering Cohort – Practical Readiness Assignment

This assignment is designed to test your understanding of everything covered so far.
You are expected to complete all tasks independently.

---

## 🔹 Section 1: Python Fundamentals

### **Exercise 1: Lists**

* Create a list of prices.
* Print the first price.
* Print the last price.
* Add a new price: `3000`.
* Sort the prices.
* Print the total of all prices.

---

### **Exercise 2: Dictionaries**

Given:

```python
customer = {
    "name": "Tunde Balogun",
    "age": 32,
    "city": "Abuja"
}
```

* Add a new key: `email` with value `"tunde@email.com"`
* Update the age to `33`
* Print all keys in the dictionary
* Check if the key `"phone"` exists

---

### **Exercise 3: Grade Calculator**

Write a program that assigns a grade based on a score.

Grading system:

* 90 and above → A
* 80 and above → B
* 70 and above → C
* Below 70 → F

Use:

```python
score = 85
```

---

### **Exercise 4: Loop Through Prices**

Given:

```python
prices = [1000, 2500, 500, 7500, 1200]
```

* Use a loop to calculate the total price.

---

### **Exercise 5: Filter Data**

Given:

```python
cities = ["Lagos", "Abuja", "London", "Kano", "Lisbon"]
```

* Print only cities that start with `"L"`

---

### **Exercise 6: Count Even Numbers**

Given:

```python
numbers = [10, 15, 20, 25, 30, 35]
```

* Count how many even numbers are in the list.

---

## 🔹 Section 2: Functions

### **Exercise 7: Filter Even Numbers**

* Write a function that takes a list and returns only even numbers.

---

### **Exercise 8: Data Validation**

* Write a function `is_valid_age(age)` that returns:

  * `True` if age is between 0 and 120
  * `False` otherwise

---

### **Exercise 9: Clean Customer Names**

* Write a function that:

  * Removes extra spaces
  * Capitalizes names properly

Example:

```
"  ahmed hassan  " → "Ahmed Hassan"
```

---

### **Exercise 10: Extract First Name**

* Write a function that extracts the first name from a full name.

Given:

```python
names = ["Ahmed Hassan", "Chioma Obi", "Emeka Nwosu"]
```

Expected output:

```
Ahmed
Chioma
Emeka
```

---

### **Exercise 11: Word Frequency Counter**

Given:

```python
text = "data data engineering is fun engineering is important"
```

* Count how many times each word appears
* Store the result in a dictionary

---

## 🔹 Section 3: File Handling (CSV)

### **Exercise 12: Read and Filter CSV**

Create a file `customers.csv`:

```csv
customer_id,name,city,total_spent
1,Ahmed Hassan,Lagos,50000
2,Chioma Obi,Abuja,75000
3,Emeka Nwosu,Lagos,30000
```

* Read the file
* Print only customers from Lagos

---

### **Exercise 13: Write CSV**

* Create a CSV file named `products.csv`
* It should contain:

  * product_id
  * name
  * price

Use at least 3 products.

---

## 🔹 Section 4: Error Handling

### **Exercise 14: Safe Division**

* Write a function `safe_divide(a, b)` that:

  * Returns the result of division
  * Handles division by zero
  * Handles invalid input types

---

### **Exercise 15: Input Validation**

* Write a function that:

  * Asks a user for their age
  * Ensures the input is a number
  * Ensures the age is between 0 and 120
  * Keeps asking until valid input is entered

---

## 📌 Submission Guidelines

* Submit your work as:

  * A `.py` file OR
  * A GitHub repository (preferred)
* Ensure your code is well-structured and readable
* Add comments where necessary

---