product = input()
location = input()
kolichestvo = float(input())
price = 0

if location == 'Sofia':
    if product == 'coffee':
        price = kolichestvo * 0.5
    elif product == 'water':
        price = kolichestvo * 0.8
    elif product == 'beer':
        price = kolichestvo * 1.2
    elif product == 'sweets':
        price = kolichestvo * 1.45
    elif product == 'peanuts':
        price = kolichestvo * 1.6

elif location == 'Plovdiv':
    if product == 'coffee':
        price = kolichestvo * 0.4
    elif product == 'water':
        price = kolichestvo * 0.7
    elif product == 'beer':
        price = kolichestvo * 1.15
    elif product == 'sweets':
        price = kolichestvo * 1.3
    elif product == 'peanuts':
        price = kolichestvo * 1.5

elif location == 'Varna':
    if product == 'coffee':
        price = kolichestvo * 0.45
    elif product == 'water':
        price = kolichestvo * 0.7
    elif product == 'beer':
        price = kolichestvo * 1.1
    elif product == 'sweets':
        price = kolichestvo * 1.35
    elif product == 'peanuts':
        price = kolichestvo * 1.55

print(price)