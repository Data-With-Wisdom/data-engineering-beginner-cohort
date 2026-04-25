import pandas as pd

# Read from CSV
df_csv = pd.read_csv('../datasets/employees.csv')
# print(df_csv)


print("\n\nREADING FROM JSON ... \n\n")

# READ from JSON
# df_json = pd.read_json('../datasets/employees.json')
# print(df_json)


# READ from POSTGRES
...


# ------------------ Inspect our data
print(df_csv.head(100))
print("\n\n")
# print(df_csv.tail(100))

# print("\n\n")

# print(df_csv.info())

# print("\n\n")


# print(df_csv.describe())


# -------------------


print(df_csv.isnull())

print("\n\n")

print(df_csv["Age"])

df_csv["Age"] = df_csv["Age"].replace('thirty', 30)
df_csv["Age"] = df_csv["Age"].astype(float)

df_csv["Age"] = df_csv["Age"].fillna(df_csv["Age"].mean())

print(df_csv["Age"])


print("\n\n")


df_csv["Salary"] = df_csv["Salary"].fillna(df_csv["Salary"].mean())

print(df_csv["Salary"])

print("\n\n")

df_csv["Department"] = df_csv["Department"].fillna("Unknown")

print(df_csv["Department"])

df_csv = df_csv.rename(columns={"Name": "Firstname", "Salary": "Amount"})

print(df_csv)

print(df_csv.info())

df_csv.shape