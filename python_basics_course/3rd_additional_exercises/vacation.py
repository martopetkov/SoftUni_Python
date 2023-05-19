budjet = float(input())
season = input()

location = ''
staying_place = ''
price = 0

if 1000 >= budjet:
    staying_place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budjet * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budjet * 0.45
elif 1000 < budjet <= 3000:
    staying_place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budjet * 0.8
    elif season == 'Winter':
        location = 'Morocco'
        price = budjet * 0.6
elif budjet > 3000:
    staying_place = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budjet * 0.9
    elif season == 'Winter':
        location = 'Morocco'
        price = budjet * 0.9

print(f'{location} - {staying_place} - {price:.2f}')