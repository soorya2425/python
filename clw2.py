# Multiline string for receipt header
header = """\tBook Store Receipt
--------------------------------------

"""

# Book details using format()
item1 = "\tBook: {}\tPrice: ₹{}\n".format("Python Basics", 450)

item2 = "\tBook: {}\tPrice: ₹{}\n".format("Data Science Intro", 600)

# Calculate total price
total = 450 + 600

# Total line
total_line = "\n\tTotal Price: ₹{}\n".format(total)

# Thank you message using concatenation
message = "\n\tThank You For Shopping With Us!"

# Combine all parts
receipt = header + item1 + item2 + total_line + message

# Display receipt in uppercase
print(receipt.upper())