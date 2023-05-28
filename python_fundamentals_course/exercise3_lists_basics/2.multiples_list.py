factor = int(input())
count = int(input())

result = []
for num in range(1, count + 1):
    result.append(num * factor)

print(result)


#vtori nachin
factor = int(input())
count = int(input())
result = []

for num in range(factor, factor * count + 1, factor):
    result.append(num)
print(result)