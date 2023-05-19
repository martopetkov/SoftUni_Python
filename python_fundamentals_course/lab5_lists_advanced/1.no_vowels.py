text = input()
result = [char for char in text if char not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(result))

#po-dobur variant
text = input()
remove_letters = ['a', 'o', 'u', 'e', 'i']

result = [char for char in text if char not in remove_letters]
print(''.join(result))