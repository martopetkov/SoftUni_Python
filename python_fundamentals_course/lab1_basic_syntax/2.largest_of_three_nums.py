num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print(f"{num1}")
elif num2 > num1 and num2 > num3:
    print(f"{num2}")
else:
    print(f"{num3}")