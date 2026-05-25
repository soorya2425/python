
fruits = ["Apple", "Banana", "Orange"]
vegetables = ["Carrot", "Potato", "Tomato"]
beverages = ["Tea", "Coffee", "Water"]

fruits.append("kiwi")


vegetables.insert(1, "cucumber")


beverages.pop()

inventory = [fruits, vegetables, beverages]


print("First two fruits:", fruits[:2])


print("Last vegetable:", vegetables[-1])


fruit_lengths = [len(item) for item in fruits]
print("Lengths of fruit names:", fruit_lengths)


print("Is Water in beverages?", "Water" in beverages)


first_items = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items)


print("Inventory:", inventory)