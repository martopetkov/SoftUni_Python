n = int(input())

for num in range(1, n + 1):
    is_special = False
    num_as_str = str(num)
    sum_digits = 0

    # Calculate sum digits
    for char in num_as_str:
        sum_digits += int(char)

    # decide if it's special
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True

    print(f"{num} -> {is_special}")

# в скобите слагаме is_special, Което се променя true/false и няма нужда от else
# condition. Вабно е, че принта е извън иф-а.
