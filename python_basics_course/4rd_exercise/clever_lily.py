age = int(input())
washer_price = float(input())
toy_price = int(input())

money = 0
money_for_year = 10
toys_number = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money += money_for_year
        money -= 1
        money_for_year += 10
    else:
        money += toy_price

diff = abs(money - washer_price)

if money >= washer_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')