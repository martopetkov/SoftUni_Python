from math import ceil
from math import floor

number_of_magnolii = int(input())
number_of_zumbules = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
gift_price = float(input())

order_sum = number_of_magnolii * 3.25 + number_of_zumbules * 4 + number_of_roses * 3.5 + number_of_cactuses * 8
taxes = order_sum * 0.05
profit = order_sum - taxes

diff = abs(gift_price - profit)

if profit >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")