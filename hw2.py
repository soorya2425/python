
paragraph = """
Python is a powerful and easy-to-learn programming language.
This Python course helps beginners understand coding concepts,
data structures, functions, and object-oriented programming.
The course also includes practical examples and projects.
"""

paragraph = paragraph.strip()

print("Length of paragraph:", len(paragraph))


print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview:", paragraph[:50])

updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", updated_paragraph)


print("\nLowercase paragraph:\n", paragraph.lower())


words = paragraph.split()
print("\nList of words:")
print(words)


if "course" in paragraph:
    print("\nThe word 'course' was found in the paragraph.")
else:
    print("\nThe word 'course' was not found.")


print(
    "\nThe course description is {} characters long and has {} words.".format(
        len(paragraph), len(words)
    )
)