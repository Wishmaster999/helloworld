import random

highest = 10
answer = random.randint (1, highest)
#print(answer)
print ("Please guess number between 1 and {}: ".format(highest))

guess = int(input())
if guess == answer:
    print ("You got it first time!")

while guess != answer:

    if guess == answer:
        print ("Well, you guessed it!")
        break
    else:
        if guess < answer:
            print ("Sorry, you have not guessed correctly, press 0 if you would like to stop the game")
            print ("Please guess higher")
        else:
            print ("Sorry, you have not guessed correctly, press 0 if you would like to stop the game")
            print ("Please guess lower")
        guess = int(input())
        if guess == answer:
            print ("Well, you guessed it!")
        if guess == 0:
            print ("Game over, you've decided to give up")
            break




