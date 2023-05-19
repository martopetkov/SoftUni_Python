trip_price = float(input())
puzzels = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())


total_price = puzzels * 2.6 + dolls * 3 + bears * 4.1 + minions * 8.2 + trucks * 2
number_of_toys = puzzels + dolls + bears + minions + trucks
if number_of_toys >= 50:
    total_price *= 0.75
rent = 0.1 * total_price
profit = total_price - rent
diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f'Yes! {diff:.2f} lv left.')
else:
    print(f'Not enough money! {diff:.2f} lv needed.')
