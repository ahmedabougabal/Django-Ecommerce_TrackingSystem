import csv
import random
from faker import Faker

fake = Faker()

status_options = ['requested', 'preparing', 'delivering', 'delivered']

# Generate 10 records of dummy data
data = []
for i in range(1, 11):
    orderID = f"ORD-{i:03d}"
    orderName = f"Order {fake.word().capitalize()}"
    username = fake.user_name()
    status = random.choice(status_options)
    data.append([orderID, orderName, username, status])

# Write the data to a CSV file
filename = 'dummy_orders.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['OrderID', 'OrderName', 'Username', 'Status'])  # Write header
    writer.writerows(data)

print(f"CSV file '{filename}' has been created with 10 records of dummy data.")















