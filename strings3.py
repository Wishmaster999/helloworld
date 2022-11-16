number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
print(values)

print()

number = "9,223;372:036 854,775;807"
separators = ""
print(separators)

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

print('----+++')

number = input("Please enter a series of numbers, using any separators you like:   ")
separators = ""
print(separators)

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

print("Excercise below to extract only capital letters: ")

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,   
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
separators = ""
print(separators)

for char in quote:
    if char.isupper():
        separators = separators + char

print(separators)