n = int(input())

positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_nums.append(number)
    else:
        negative_nums.append(number)
    if number % 2 == 0:
        even_nums.append(number)
    else:
        odd_nums.append(number)

command = input()
if command == "positive":
    print(positive_nums)
elif command == 'negative':
    print(negative_nums)
elif command == 'even':
    print(even_nums)
else:
    print(odd_nums)