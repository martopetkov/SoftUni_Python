budjet = float(input())
season = input()
location = ''
place = ''
price = 0

if budjet <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        price = budjet * 0.3
        place = "Camp"
    elif season == 'winter':
        price = budjet * 0.7
        place = 'Hotel'

elif budjet <= 1000:
    location = 'Balkans'
    if season == 'summer':
        price = budjet * 0.4
        place = "Camp"
    elif season == 'winter':
        price = budjet * 0.8
        place = 'Hotel'

elif budjet > 1000:
    location = 'Europe'
    price = budjet * 0.9
    place = 'Hotel'

print(f'Somewhere in {location}')
print(f'{place} - {price:.2f}')