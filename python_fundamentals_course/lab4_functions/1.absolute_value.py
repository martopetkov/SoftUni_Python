#1ви начин
print([abs(float(el)) for el in input().split()])

#2ри начин
numbers_as_string = input().split()
numbers = []
for el in numbers_as_string:
    numbers.append(abs(float(el)))

print(numbers)