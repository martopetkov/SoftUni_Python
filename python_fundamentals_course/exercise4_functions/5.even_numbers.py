def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


numbers = [int(x) for x in input().split()]
even_nums_iterator = filter(check_even, numbers)
even_nums = list(even_nums_iterator)
print(even_nums)


#2ri nachin
def check_even(num):
    result = num % 2 == 0
    return result


numbers = [int(x) for x in input().split()]
print(list(filter(check_even, numbers)))