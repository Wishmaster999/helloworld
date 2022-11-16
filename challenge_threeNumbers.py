values = input ("Please enter three numbers: ")

values_list = values.split()

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

a = []
b = []
c = []

for i in values_list:
    a.append(values_list[0])
    b.append(values_list[1])
    c.append(values_list[2])
    break

stringsA = [str(integer) for integer in a]
a_string = "".join(stringsA)
a = int(a_string)
stringsB = [str(integer) for integer in b]
b_string = "".join(stringsB)
b = int(b_string)
stringsC = [str(integer) for integer in c]
c_string = "".join(stringsC)
c = int(c_string)


calculation = (a + b - c)
print("Your result of calculation is: ", calculation)




