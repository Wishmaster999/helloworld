todo_list = ['dummy', 'Learn Python', 'Learn Java', 'Go swimming', 'Have dinner', 'Go to bed']

print("""Please choose your option from the list below: \t
1. \tLearn Python \t
2. \tLearn Java \t
3. \tGo swimming \t
4. \tHave dinner \t
5. \tGo to bed \t
0. \tExit""")

while True:
    try:
        answer = int(input("Enter a number: "))
        if isinstance(answer, int) and answer >= 0:
            break
    except ValueError:
        print('An error occured! Input an integer!')



while answer != 0:
        if 0 < answer <= 5:
            print ("Well, you choose to {}!".format(todo_list[answer]))
            break
        else:
            print("Please choose the valid option!")
            answer = int(input())

if answer == 0:
    print ("You terminated the program!")


##new approach below:
print ("*+"*70)
answer = "-"
while answer !="0":
    if answer in "12345":
        print("You choose {}".format(answer))
    else:
        print('Please choose your option from the list below:')
        print("1. \tLearn Python")
        print("2. \tLearn Java")
        print("3. \tGo swimming")
        print("4. \tHave dinner")
        print('5. \tGo to bed')
        print("0. \tExit")

    answer = input("Enter a number: ")

