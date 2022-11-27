available_parts = [
    ("computer",
     [
         (500),
     ]
     ),
    ("monitor",
     [
         (300),
     ]
     ),
    ("keyboard",
     [
         (25),
     ]
     ),
    ("mouse",
     [
         (10),
     ]
     ),
    ("mouse mat",
     [
         (6),
     ]
     ),
    ("HDMI cable",
     [
         (8),
     ]
     ),
    ("DVD drive",
     [
         (13),
     ]
     ),
]
articles = []
price = []

for part in available_parts:
    articles.append(part[0])
    price.append(part[1][0])
print(articles)
print(price)

valid_choices = []
current_choice = "-"
computer_parts = [] # create an empty list
total_price = []

valid_choices = []
for i in range (1, len(articles) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:
        index = int (current_choice) - 1
        chosen_part = articles[index]
        chosen_price = price[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
            total_price.remove(chosen_price)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
            total_price.append(chosen_price)
        print ("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(articles):
            print("{0}: {1}".format(number + 1, part))
        print("Enter a number: ")

    current_choice = input()

print("Your shopping list: ", computer_parts)

for i in range(0, len(total_price)):
    total_price[i] = int(total_price[i])
print("Total price of chosen items: ", sum(total_price))
