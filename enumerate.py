for index, character in enumerate ('abcdefgh'):
    print(index, character)

#for character in enumerate ('abcdefgh'):
#    print(character)


for t in enumerate ('abcdefgh'):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)