def perfect_number(num):
    is_perfect = True
    sum = 0
    for divisor in range(1, num//2 + 1):
        if num % divisor == 0:
            sum += divisor
    if sum != num:
        is_perfect = False

    return is_perfect


number = int(input())
is_perfect = perfect_number(number)
if is_perfect:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
