result = True
another_result = result
print(id(result))
print(id(another_result))

print("^"*70)

result = False
another_result = result
print(id(result))
print(id(another_result))

print("^"*70)

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))