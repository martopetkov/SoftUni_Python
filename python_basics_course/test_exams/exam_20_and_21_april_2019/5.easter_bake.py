from math import ceil
from sys import maxsize
max_sugar = -maxsize
max_flour = -maxsize

num_kozunaci = int(input())

sugar_box = 0
flour_box = 0
sugar_grams = 0
flour_grams = 0
for k in range(1, num_kozunaci + 1):
    used_sugar = int(input())
    used_flour = int(input())
    if used_sugar > max_sugar:
        max_sugar = used_sugar
    if used_flour > max_flour:
        max_flour = used_flour

    sugar_grams += used_sugar
    flour_grams += used_flour

sugar_box = ceil(sugar_grams / 950)
flour_box = ceil(flour_grams / 750)

print(f'Sugar: {sugar_box}')
print(f'Flour: {flour_box}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
