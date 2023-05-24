positives = []
negatives = []
evens = []
odds = []

integers = [int(x) for x in input().split(", ")]
for x in integers:
    if x >= 0:
        positives.append(x)
    else:
        negatives.append(x)

    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)

print(f'Positive: {", ".join([str(x) for x in positives])}')
print(f'Negative: {", ".join([str(x) for x in negatives])}')
print(f'Even: {", ".join([str(x) for x in evens])}')
print(f'Odd: {", ".join([str(x) for x in odds])}')

