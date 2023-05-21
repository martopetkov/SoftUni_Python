import sys

smallest = sys.maxsize
largest = -sys.maxsize
chisla = int(input())

for i in range (0, chisla):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

print(f'Max number: {largest}')
print(f'Min number: {smallest}')