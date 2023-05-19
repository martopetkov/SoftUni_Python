budjet = float(input())
season = input()
klas = ''
price = 0
car_type = ''
if budjet <= 100:
    klas = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budjet * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budjet * 0.65

elif 100 < budjet <= 500:
    klas = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budjet * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budjet * 0.8

elif budjet > 500:
    klas = 'Luxury class'
    car_type = 'Jeep'
    price = budjet * 0.9

print(f'{klas}')
print(f'{car_type} - {price:.2f}')