numbers = [int(x) for x in input().split()]
descending_order = sorted(numbers, key=lambda x: -x)
average = sum(numbers) / len(numbers)

result = []
counter = 0

for el in descending_order:
    if el > average:
        result.append(el)
        counter += 1

        if counter >= 5:
            break

if len(result) == 0:
    print("No")
else:
    print(*result)
