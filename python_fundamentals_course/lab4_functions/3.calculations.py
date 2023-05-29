def calculation(operation, num1, num2):
    result = None
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        result = num1 // num2
    return result


operation = input()
num1 = int(input())
num2 = int(input())

res = calculation(operation, num1, num2)
print(res)