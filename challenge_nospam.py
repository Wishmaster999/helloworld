menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam']
]
#spam = "spam"

#for eat_list in menu:
#    eat_list
#    for value in eat_list:
#        value
#    while (spam in eat_list):
#        eat_list.remove(spam)

#for eat_list in menu:
#    print(eat_list)

#print("++++++++++++++++++++++++++++++++++++++++++")

for meal in menu:
    for index in range (len(meal) -1, -1, -1):
        if meal [index] == "spam":
            del meal [index]

    print(meal)
print("++++++++++++++++++++++++++++++++++++++++++")
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=" ")
    print()










