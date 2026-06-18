from datetime import datetime
import random

customer_name = input("Enter Customer Name: ")

products = []
subtotal = 0

while True:
    product = input("Enter Product Name: ")
    qty = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    amount = qty * price
    subtotal += amount

    products.append([product, qty, price, amount])

    more = input("Add another product? (y/n): ")
    if more.lower() != 'y':
        break

gst = subtotal * 0.18
grand_total = subtotal + gst

invoice_no = random.randint(100000000000, 999999999999)
date = datetime.now().strftime("%d-%m-%Y %H:%M")

filename = f"Invoice_{invoice_no}.txt"

with open(filename, "w") as file:
    file.write("=" * 60 + "\n")
    file.write("INVOICE\n")
    file.write("=" * 60 + "\n\n")

    file.write(f"Customer: {customer_name}\n")
    file.write(f"Date: {date}\n")
    file.write(f"Invoice No: {invoice_no}\n")
    

    file.write("-" * 60 + "\n")
    file.write(f"{'Product':<20}{'Qty':<10}{'Price':<12}{'Amount':<10}\n")
    file.write("-" * 60 + "\n")

    for item in products:
        file.write(
            f"{item[0]:<20}{item[1]:<10}{item[2]:<12.2f}{item[3]:<10.2f}\n"
        )

    file.write("-" * 60 + "\n")
    file.write(f"{'':35}Subtotal: {subtotal:.2f}\n")
    file.write(f"{'':35}GST (18%): {gst:.2f}\n")
    file.write(f"{'':35}Grand Total: {grand_total:.2f}\n")
    file.write("=" * 60 + "\n")

print(f"Invoice generated successfully: {filename}")