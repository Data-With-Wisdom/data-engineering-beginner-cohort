# name = input("Please enter your name: ")
# print(f"Welcome to a simple python progam, {name} !")

# -------------------- COMMENTS --------------------
# Single -> Comment

"""
Multi-line
Write whatever you want to write here.
"""

'''
sahddksd
'''


# ----------------- Variables ----------------
firstname = "wisdom"
lastname = "nwachukwu"
single_quote = 'Single Quote Test'
tripple_quotes = """
    One with double quotation marks
"""
tripple_quotes_2 = '''
    One with tripple single quotes
'''


age = 26
year = 2026
degree = 38.89
negative_degree = -17.5


empty_value = None

print(firstname, lastname)


# -------------- Type Checking -----------------
print('-------------- Type Checking -----------------')
print(type(firstname))
print(type(single_quote))
print(type(tripple_quotes))
print(type(tripple_quotes_2))


print(type(age))
print(type(degree))
print(type(negative_degree))


print(type(empty_value))


# --------------------- Type Conversion -----------------------

print('--------------------- String to Interger Type Conversion -----------------------')
string_value = "25"
_value = int(string_value)
print(_value, type(_value))


print('--------------------- Interger to String Type Conversion -----------------------')
int_to_str_value = str(1000)
print(type(int_to_str_value))


print('--------------------- String to Float Type Conversion -----------------------')
str_to_float_value = float("233.3434")
print(type(str_to_float_value))

float(), str(), int(), 
bool() # ---- Used for evaluation; Not used for conversion

# print(bool(3 > 4))
print(bool(0.1))


age = "25"
print(int(age) + 5)



# -------------------- Operators -----------
print('-------------------- Arithemethic Operators -----------')
print(4 // 2) # n times it appears
print(90 // 4) # 
print(30 % 3) # r - 0
print(2 ** 2)


print('-------------------- Comparison Operators -----------')
print(45 > 40)




print('-------------------------- Logical Operator ----------------------')
# and, or, not

print(not 4 < 2)
print('wisdom' is 'wisdom') # is 2 equal to 3 in data type and value? 2 === 3


print('------------------------- Assignment Ops ----------------------')
x = 10
# x = x + 5
# x = x - 5
# x = x / 5

x /= 5

print(int(x))




print('---------------------------- String Ops -----------------------------')
# Concatenation 
name = "wisdom"
surname = "nwachukwu"

print("My name is " + name + " and my surname is " + surname)

# Repitition
print("ha " * 10)


# String Formatting: F-String
print(f"My name is {name} and my surname is {surname}")
print(f"Price is: {2 * 3 * 0.075}")

# age = 5 + "25"
# print(age)



# -------------------------- Data Structure ----------------------------
# LIST: A list stores multiple items in order.

# customer = 'wisdom'
customers = ['Wisdom', 'Gbenga', 'Emzzy', 'Sodiq', 'Pascal'] # ordered; can hold multiple data types
cities = ['Lagos', 'Abuja']



# ---- Access list items
print(customers[-5])


# ---- Operation in list -------
# Length
print(len(cities))

# Add into a list
basket = []

basket.append('Apple')
basket.append('Orange')
basket.append('Banana')
print(basket)

basket.remove("Apple")
print(basket)

basket.pop(0)
print(basket)