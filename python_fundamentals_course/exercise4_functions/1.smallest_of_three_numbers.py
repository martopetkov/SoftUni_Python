def smallest_number(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        result = num1
    elif num2 < num1 and num2 < num3:
        result = num2
    else:
        result = num3
    return result


num1 = int(input())
num2 = int(input())
num3 = int(input())
the_smallest = smallest_number(num1, num2, num3)
print(the_smallest)

# vtori nachin
def smallest_number(numbers):
    min_number = float('inf')
    for num in numbers:
        if num < min_number
            min_number = num
    return min_number

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest_number([num1, num2, num3]))

# treti nachin
def smallest_number(numbers):
    return min(numbers)

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(smallest_number([num1, num2, num3]))