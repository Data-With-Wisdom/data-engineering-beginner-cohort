import csv, json

"""
READ FROM CSV
"""
# METHOD: 1

# with open(file="../0-data/source/customers.csv", mode="r") as file:
#     # print(file)
#     csv_reader = csv.reader(file)
#     # print(csv_reader)

#     # csv: consists of a header and the actual data
#     # Skip header and hold in memory
#     header = next(csv_reader)
#     print(f"HEADER: {header}")

#     # Loop over actual data; Each data in the CSV file
#     for row in csv_reader:
#         print(row)


# METHOD 2: READ FROM CSV

# with open(file="../0-data/source/customers.csv", mode="r") as my_file:
#     csv_reader = csv.DictReader(my_file)
#     # print(type(csv_reader))

#     for row in csv_reader:
#         print(f"{row['customer_id']} -- {row['name']}")
        

'''
Write into CSV
'''
# Method 1:
# data = [
#     ['customer_id', 'name', 'city'],
#     [1, 'Ahmed Hassan', 'Lagos'],
#     [2, 'Chioma Obi', 'Abuja']
# ]

# with open(file='../0-data/outputs/output1.csv', mode='w', newline='') as written_file:
#     csv_writer = csv.writer(written_file)
#     csv_writer.writerows(data)


# Method 2:
# customers = [
#     {'customer_id': 1, 'name': 'Ahmed Hassan', 'city': 'Lagos'},
#     {'customer_id': 2, 'name': 'Chioma Obi', 'city': 'Abuja'}
# ]

# with open(file='../0-data/outputs/_output1.csv', mode='w', newline='') as written_file:
#     field_names = ['customer_id', 'name', 'city']
#     csv_writer = csv.DictWriter(written_file, fieldnames=field_names)

#     csv_writer.writeheader()
#     csv_writer.writerows(customers)




# ------------ JSON ------------




# Read JSON file
# with open(file='../0-data/source/customer.json', mode='r') as file:
#     data = json.load(file)

# print(data['name'])  # Ahmed Hassan
# print(data['orders'][0]['amount'])  # 5000

# # Access nested data
# for order in data['orders']:
#     print(f"Order {order['order_id']}: ₦{order['amount']}")


import csv, json
# from json import dump

# Read CSV
# with open('../0-data/source/customers.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     print(csv_reader)
#     customers = list(csv_reader)
#     print(customers)

# # Write JSON
# with open('../0-data/outputs/new_json.json', "w") as json_file:
#     json.dump(customers, json_file, indent=4)


# print("Converted CSV to JSON")



import os

# if os.path.exists('../0-data/source/customers.csv'):
#     print("File exists!")
# else:
#     print("File not found!")



# ===================== Error Handling ==================

# age = 0

# if age > 18 # ❌ SyntaxError: invalid syntax
#     print("Adult")


# Note: Syntax error is not caught by the try...except, likewise the NameError
# try:
#     age = 0

#     if age > 18: # SyntaxError: invalid syntax
#         print("Adult")

#     age = int(input("Enter your age: "))
#     print(f"You are {age} years old")
# except Exception:
#     print("Invalid input. Please enter a number.")


try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")
except KeyboardInterrupt:
    print("\nProgram cancelled by user")