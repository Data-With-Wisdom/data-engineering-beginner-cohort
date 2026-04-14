import csv

source_csv_file = "../0-data/source/customers.csv"
output_file = '../0-data/outputs/cleaned_customers_data.csv'

with open(file=source_csv_file, mode="r") as file_object:
    csv_reader = csv.DictReader(file_object)

    cleaned_data = []

    for row in csv_reader:
        
        cleaned = {
            "customer_id": int(row['customer_id']),
            "name": str(row['name']).title(),
            "city": str(row['city']).title(),
            "email": str(row['email']),
            "total_spent": float(row['total_spent'])
        }
        # print(cleaned)
        cleaned_data.append(cleaned)
    print(cleaned_data)
        
# Write cleaned_data

with open(file=output_file, mode="w", newline='') as file:
    field_names = ['customer_id', 'name', 'city', 'email', 'total_spent']

    csv_writer = csv.DictWriter(file, fieldnames=field_names)
    csv_writer.writeheader()
    csv_writer.writerows(cleaned_data)

print(f"{source_csv_file}'s data has been processed and written into a new CSV file '{output_file}'!")
