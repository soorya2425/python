
web_development = ["Rahul", "Anu", "Vivek"]
data_science = ["Meera", "Asha", "Kiran"]
ui_ux_design = ["Sneha", "Arjun", "Diya"]


all_participants = [web_development, data_science, ui_ux_design]


web_development.append("Nithin")


data_science.insert(1, "Riya")


ui_ux_design.pop()


data_science_copy = data_science.copy()
data_science.clear()


print("First two Web Development participants:", web_development[: 2])


name_lengths = [len(name) for name in data_science_copy]
print("Length of each Data Science participant name:", name_lengths)

asha_exists = (
    "Asha" in web_development or
    "Asha" in data_science_copy or
    "Asha" in ui_ux_design
)
print("Is Asha in any workshop?", asha_exists)


first_participants = (
    web_development[0],
    data_science_copy[0],
    ui_ux_design[0]
)

print("Tuple of first participants:", first_participants)

print("\nAll Participants:", all_participants)
print("Copied Data Science List:", data_science_copy)
print("Original Data Science List after clear:", data_science)