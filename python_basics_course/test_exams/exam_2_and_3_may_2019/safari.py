budjet = float(input())
fuel_liters = float(input())
day_of_the_week = input()


fuel_price = fuel_liters * 2.1
fuel_with_ekskurzovod = fuel_price + 100

if day_of_the_week == 'Saturday':
    fuel_with_ekskurzovod *= 0.9
elif day_of_the_week == 'Sunday':
    fuel_with_ekskurzovod *= 0.8

diff = abs(budjet - fuel_with_ekskurzovod)

if budjet >= fuel_with_ekskurzovod:
    print(f'Safari time! Money left: {diff:.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')