import random

rice_price = 45
sugar_price = 40
oil_price = 130


rice_qty = 3
sugar_qty = 2.5
oil_qty = 1.8


rice_total = float(rice_price) * rice_qty
sugar_total = float(sugar_price) * sugar_qty
oil_total = float(oil_price) * oil_qty


print("Rice Total: ₹", rice_total)
print("Sugar Total: ₹", sugar_total)
print("Oil Total: ₹", oil_total)

total_bill = rice_total + sugar_total + oil_total

print("\nTotal Bill: ₹", total_bill)


bill_int = int(total_bill)
print("Total Bill as Integer: ₹", bill_int)


bill_str = str(total_bill)
print("Total Bill as String: ₹" + bill_str)


delivery_charge = random.randint(5, 10)

print("\nDelivery Charge: ₹", delivery_charge)


final_bill = total_bill + delivery_charge

print("Final Bill Including Delivery: ₹", final_bill)