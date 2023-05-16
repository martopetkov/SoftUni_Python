def odd_and_even(number):
    odd_numbers = 0
    even_numbers = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_numbers += int(digit)
        else:
            odd_numbers += int(digit)
    return odd_numbers, even_numbers


n = input()
sum_odd, sum_even = odd_and_even(n)
print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")