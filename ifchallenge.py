name = input('Please enter your name?  ')
age = int(input('Please enter your age?  '))

if 18 <= age <= 30:
    print("Welcome to the holidays for 18-30 years old, {}".format(name))
else:
    print("Sorry, you are not allowed to enter, {}".format(name))