def sum_numbers(a, b):
    return a + b


def subtract(sum, c):
    return sum - c


def add_and_subtrack(a, b, c):
    sum_of_a_and_b = sum_numbers(a, b)
    result = subtract(sum_of_a_and_b, c)
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtrack(num1, num2, num3))



