shirt_price = float(input())
needed_sum = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (shirt_price + shorts_price) * 2

total_sum = shirt_price + shorts_price + socks_price + shoes_price
after_discount = total_sum * 0.85

diff = abs(after_discount - needed_sum)
if after_discount >= needed_sum:
    print('Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {after_discount:.2f} lv.')
else:
    print('No, he will not earn the world-cup replica ball.')
    print(f'He needs {diff:.2f} lv. more.')