available_parts = [
    ("computer",
     [
         (500, "USD"),
     ]
     ),
    ("monitor",
     [
         (300, "USD"),
     ]
     ),
    ("keyboard",
     [
         (25, "USD"),
     ]
     ),
    ("mouse",
     [
         (10, "USD"),
     ]
     ),
    ("mouse mat",
     [
         (6, "USD"),
     ]
     ),
    ("HDMI cable",
     [
         (8, "USD"),
     ]
     ),
    ("DVD drive",
     [
         (13, "USD"),
     ]
     ),
]
articles = available_parts
for article, price in articles:
    print("Article: {0}, Price: {1}".format(article, price))
    print(article)

current_choice = "-"
computer_parts = [] # create an empty list

valid_choices = []
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:
        index = int (current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print ("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
        print("Enter a number: ")

    current_choice = input()

print(computer_parts)
