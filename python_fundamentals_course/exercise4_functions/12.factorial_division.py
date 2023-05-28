def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

num1 = int(input())
num2 = int(input())

first_factorial = factorial(num1)
second_factorial = factorial(num2)

result = first_factorial / second_factorial
print(f"{result:.2f}")

#втори начин на фор цикъла в деф-а (съкратен)
def factorial(n):
    for i in range(1, n + 1):
        n *= i
    return n