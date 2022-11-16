for i in range (1, 13):
    print ("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))
    print("*" * 10)
print("*" * 10)

name = input ("Please enter your name:  ")
age = int(input ("How old are you, {0}?".format (name)))
print ("Your age is {0}, {1}!".format(age, name))

#if age >= 18:
#    print("You're old is enough to vote!")
 #   print("Please put an X in the box")
#else:
 #   print("Please come back in {0} year/s!".format(18-age))

if age < 18:
    print("Please come back in {0} year/s!".format(18-age))
elif age == 900:
    print("Sorry, Yoda")
else:
    print("You're old is enough to vote!")
    print("Please put an X in the box")
