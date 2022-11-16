values = input ("Please enter three numbers: ")

values_list = values.split()

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

entries = []


for i in values_list:
    entries.append(int(i))

print(entries)

a, b, c = entries

result = a + b - c

print(result)