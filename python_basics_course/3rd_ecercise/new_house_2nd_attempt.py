flower_type = input()
flower_number = int(input())
budjet = int(input())
price = 0
discount = 0

if flower_type == 'Roses':
    price += 5
    if flower_number > 80:
        discount += 0.1

elif flower_type == 'Dahlias':
    price += 3.8
    if flower_number > 90:
        discount += 0.15

elif flower_type == 'Tulips':
    price += 2.8
    if flower_number > 80:
        discount += 0.15

elif flower_type == 'Narcissus':
    price += 3
    if flower_number < 120:
        discount -= 0.15

elif flower_type == 'Gladiolus':
    price += 2.5
    if flower_number < 80:
        discount -= 0.2

total_price = price * flower_number * (1 - discount)
diff = abs(total_price - budjet)

if total_price >= budjet:
    print(f'Hey, you have a great garden with {flower_number} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')