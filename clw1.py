import random


apple_juice = 15.5
orange_juice = 20
grape_juice = 10.25

total_volume = apple_juice + orange_juice + grape_juice

print("Total Volume:", total_volume)


total_int = int(total_volume)
print("Integer Value:", total_int)

total_str = str(total_volume)
print("Total Volume Sold: " + total_str + " liters")

bonus = random.randint(5, 10)

final_total = total_volume + bonus

print("Bonus Liters:", bonus)
print("Final Total Volume:", final_total)