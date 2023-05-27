number = int(input())

for i in range(number):
    for k in range(number):
        for j in range(number):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")


# vtori nachin

number = int(input())
start = 97

for i in range(start, start + number):
    for k in range(start, start + number):
        for j in range(start, start + number):
            print(f"{chr(i)}{chr(k)}{chr(j)}")
