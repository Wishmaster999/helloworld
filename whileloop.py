for i in range(10):
    print("i is now {0}".format(i))
    if i == 8:
        break

print("++++++++++++++++")

i = 0
while i < 10:
    print("i is now {0}".format(i))
    #i += 1
    i = i + 1       #the same as previous line

#excercise
#Modify the code so that it stops printing when it reaches a number greater than zero that's exactly divisible by 11.
#That number should be the last value printed.
#Reminder: If a value, x, is divisible by 11 then x % 11 will be zero.
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i%11 == 0:
        break
#excercise
for i in range(0, 20):
    if i==0 or (i%3!=0 and i%5!=0):
        print (i)
# using continue
for i in range(0, 20):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)






