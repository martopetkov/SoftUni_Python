month = input()
nights = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio = nights * 50
    price_apartment = nights * 65
    if 7 < nights < 14:
        price_studio *= 0.95
    elif nights > 14:
        price_studio *= 0.70
        price_apartment *= 0.9

elif month == 'June' or month == 'September':
    price_studio = nights * 75.20
    price_apartment = nights * 68.70
    if 14 < nights:
        price_studio *= 0.80
        price_apartment *= 0.9

elif month == 'July' or month =='August':
    price_studio = nights * 76
    price_apartment = nights * 77
    if nights > 14:
        price_apartment *= 0.9

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')