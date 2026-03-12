# # name = input("Please enter your name: ")
# # print(f"Welcome to a simple python progam, {name} !")

# # -------------------- COMMENTS --------------------
# # Single -> Comment

# """
# Multi-line
# Write whatever you want to write here.
# """

# '''
# sahddksd
# '''


# # ----------------- Variables ----------------
# firstname = "wisdom"
# lastname = "nwachukwu"
# single_quote = 'Single Quote Test'
# tripple_quotes = """
#     One with double quotation marks
# """
# tripple_quotes_2 = '''
#     One with tripple single quotes
# '''


# age = 26
# year = 2026
# degree = 38.89
# negative_degree = -17.5


# empty_value = None

# print(firstname, lastname)


# # -------------- Type Checking -----------------
# print('-------------- Type Checking -----------------')
# print(type(firstname))
# print(type(single_quote))
# print(type(tripple_quotes))
# print(type(tripple_quotes_2))


# print(type(age))
# print(type(degree))
# print(type(negative_degree))


# print(type(empty_value))


# # --------------------- Type Conversion -----------------------

# print('--------------------- String to Interger Type Conversion -----------------------')
# string_value = "25"
# _value = int(string_value)
# print(_value, type(_value))


# print('--------------------- Interger to String Type Conversion -----------------------')
# int_to_str_value = str(1000)
# print(type(int_to_str_value))


# print('--------------------- String to Float Type Conversion -----------------------')
# str_to_float_value = float("233.3434")
# print(type(str_to_float_value))

# float(), str(), int(), 
# bool() # ---- Used for evaluation; Not used for conversion

# # print(bool(3 > 4))
# print(bool(0.1))


# age = "25"
# print(int(age) + 5)



# # -------------------- Operators -----------
# print('-------------------- Arithemethic Operators -----------')
# print(4 // 2) # n times it appears
# print(90 // 4) # 
# print(30 % 3) # r - 0
# print(2 ** 2)


# print('-------------------- Comparison Operators -----------')
# print(45 > 40)




# print('-------------------------- Logical Operator ----------------------')
# # and, or, not

# print(not 4 < 2)
# print('wisdom' is 'wisdom') # is 2 equal to 3 in data type and value? 2 === 3


# print('------------------------- Assignment Ops ----------------------')
# x = 10
# # x = x + 5
# # x = x - 5
# # x = x / 5

# x /= 5

# print(int(x))




# print('---------------------------- String Ops -----------------------------')
# # Concatenation 
# name = "wisdom"
# surname = "nwachukwu"

# print("My name is " + name + " and my surname is " + surname)

# # Repitition
# print("ha " * 10)


# # String Formatting: F-String
# print(f"My name is {name} and my surname is {surname}")
# print(f"Price is: {2 * 3 * 0.075}")

# # age = 5 + "25"
# # print(age)



# # -------------------------- Data Structure ----------------------------
# # LIST: A list stores multiple items in order.

# # customer = 'wisdom'
# customers = ['Wisdom', 'Gbenga', 'Emzzy', 'Sodiq', 'Pascal'] # ordered; can hold multiple data types
# cities = ['Lagos', 'Abuja']



# # ---- Access list items
# print(customers[-5])


# # ---- Operation in list -------
# # Length
# print(len(cities))

# # Add into a list
# basket = []

# basket.append('Apple')
# basket.append('Orange')
# basket.append('Banana')
# print(basket)

# basket.remove("Apple")
# print(basket)

# basket.pop(0)
# print(basket)


# # --------------

# # iterable: Anything you can loop over; 'iterate'
# fruits = ['Cherry', 'Avacado', 'Carrot', 'Coconut']

# print('cherry' in fruits)



# # ---------
# numbers = [10, 20, 30, 40, 50, 60, 70]

# # iterable[start:stop:step]

# print(numbers[0:4:1])


# # ------- SORTING A LIST-----------
# prices = [1000, 500, 2500, 500, 7500]
# prices.sort()
# print(prices)

# # --------- REVERSE a list -----------
# numbers.reverse()
# print(numbers)



# # --------- COUNT OCCURENCE
# print(prices.count(10000000))



# # --------- FIND INDEX 
# print(prices)
# print(prices.index(500))


# --------- LOOPING THROUGH LISTS 
# cities = ["Lagos", "Abuja", "Port Harcourt"]

# import time
# from threading import Thread
# import asyncio


# # for i in ["Lagos", "Abuja", "Port Harcourt"]:
# #     print(i)
# #     # time.sleep(2)
# #     if i == 'Abuja':
# #         print(f"Finally found {i}, so interpreter would stop now")
# #         break
    

# # --------------- DICTIONARY

# # key-value pair

# #------- create dictionary
# customer = {
#     "name": "Wisdom", 
#     "age": 26, 
#     "city": "Lagos"
# }
# # x = dict(name='wisdom', age=28, gender='male')
# print(customer)

# # ---- Accessing a dictionary
# print(customer["name"]) # Method: 1
# print(customer.get("age")) # Method: 1 (Safer way)

# # ---- Adding / Updating values
# customer["email"] = "crypticwisdom84@gmail.com"
# customer["gender"] = "male"
# customer['gibrish'] = 'qwerty'

# customer["name"] = "Victor" # Override
# print(customer)


# # ---- Remove Item
# # del customer['gibrish'] # Method 1
# # print(customer)


# g = customer.pop('gibrish')
# print(g, customer)


# ------ Dictionary Methods
# customer = {"name": "Ahmed", "age": 28, "city": "Lagos"}
# print(type(customer))
# print(customer.keys())
# print(customer.values())
# print(customer.items())


# # ---------- Tuples
# empty_tuple = ()
# print(type(empty_tuple))

# coordinates = (6.5244, 3.3792)
# single = (5,)  # print(type(single))


# # --------- Tuple
# coordinates = (6.5244, 3.3792)

# print(coordinates)

# # coordinates[2] = 'victor' # Errors out, tuples are immutable (cannot be changed after declaration)
# print(coordinates)

# # Only 2 Methods in tuple
# print(coordinates.count(6.5244))
# print(coordinates.index(6.5244))




# # --------------- SETs 
# # an unordered collection of unique elements.
# """
#     List -> Ordered: [1,2,3] -> [1,2,3]
#     Tuple -> Ordered (1,2,3) -> (1,2,3)
#     Set -> Unordered {1,2,3} -> {2, 1, 3}
#     Dict -> Ordered -> {}
# """
# dict
# empty_set = set() # don't use {} for an empty set, use set() instead
# print(type(empty_set))

# set_of_unique_items = {
#     1, 1, 2, 2, 3, 7, 7, 5, 9, 9, 90, 67, 3, 2, 3, 4, 3, 4, 5, 5,
# }
# print(set_of_unique_items)


# # Set method
# new_set = set_of_unique_items.copy()
# print(new_set)

# set_of_unique_items.clear()
# print(set_of_unique_items)


# kl = [12, 21, 12, 12, 45, 45, 45, 565, 565, 5, 5]
# print(set(kl))


# -------------------------------------------- Control Flow -------------------------------------------------

# order of exec is usually top-to-bottom

# age = 1
# # 1. if-stmt
# print(age >= 18)
# if age >= 18:
#     print('--------------------- Yes it is greater')

# # 2. if-else statement
# # if cond:
# #     stmt
# # else:
# #     stmt

# print(age >= 1)
# if age >= 1:
#     print('------ Hey you are welcome ---------')
#     print('---------- You qualify for the script ---------')
# else:
#     print('-------- Error: You are not eligible for running this script -------')
#     print('------------- Enter a positive number greater than  1')


# # 3. if-elif-else statement (if-elseif-else)
# print("\n\n\n\n\n")
# score = 0

# if score >= 90:
#     print("This student has a Grade A")
# elif score >= 80:
#     print("Student got Grade B")
# elif score >= 70:
#     print("Student got Grade C")
# elif score >= 60:
#     print("Student got Grade D")
# else:
#     print("Student got Grade F")



# print('----------- Out of the statement ------------')

# ------------- Logical Operators --------------
# Used for combining multiple conditions.

# Types of logical ops: and, or, not

#
# 1. and ----------------------------------------
# True and True = True
# False and True = False
# True and False = False



# age, city, country = 13, 'Lagos', 'Nigeria'

# if (age > 18) and (city == 'Lagos') and (country == 'Nigeria'):
#     print('------- Customer Qualified --------')
#     print((age > 18) and (city == 'Lagos') and (country == 'Nigeria'))
# elif age > 10:
#     print('-------- User is just 10 years old ------')
# else:
#     print('Customer is not qualified')
#     print((age > 18) and (city == 'Lagos') and (country == 'Nigeria'))




# 2: or ----------------------------------------------
# True or True = True
# True or False = True
# False or True = True
# False or False = False

age, city, country = 13, 'Lagos', 'Nigeria'

# if (age > 18 or city == 'Lagos') and (country == 'Nigeria'):
#     print('------- Customer Qualified --------')
#     print((age > 18) or (city == 'Lagos') or (country == 'Nigeria'))
# elif age > 10:
#     print('-------- User is just 10 years old ------')
# else:
#     print('Customer is not qualified')
#     print((age > 18) or (city == 'Lagos') or (country == 'Nigeria'))





#  -----------------------------------
is_verified = False
print(not is_verified)

age = 19
if not (age > 18):
    print('--------- Qualified ---------')
else:
    print('--------- Not Qualified ---------')