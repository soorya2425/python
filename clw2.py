
header = """\tBook Store Receipt
------------------------------------"""

item1 = "\tBook: {}\tPrice: ₹{}\n".format("Python Basics", 450)

item2 = "\tBook: {}\tPrice: ₹{}\n".format("Data Science Intro", 600)

total = 450 + 600

total_line = "\tTotal Price: ₹{}\n".format(total)


message = "\tThank You For Shopping With Us!"


receipt = header + item1 + item2 + total_line + message


print(receipt.upper())