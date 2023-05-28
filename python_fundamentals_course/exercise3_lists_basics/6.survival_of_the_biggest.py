list_of_integers = [int(x) for x in input().split()]
count = int(input())

for _ in range(count):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)

print(', '.join([str(x) for x in list_of_integers]))