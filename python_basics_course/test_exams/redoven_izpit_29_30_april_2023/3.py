sweet = input()
ordered_sweets = int(input())
day_of_month = int(input())

price = 0

if day_of_month <= 15:
    if sweet == 'Cake':
        price = 24
    elif sweet == 'Souffle':
        price = 6.66
    elif sweet == 'Baklava':
        price = 12.6
elif day_of_month > 15:
    if sweet == 'Cake':
        price = 28.7
    elif sweet == 'Souffle':
        price = 9.8
    elif sweet == 'Baklava':
        price = 16.98

total_sum = ordered_sweets * price
if day_of_month <= 22:
    if 100 <= total_sum <= 200:
        total_sum *= 0.85
    if total_sum > 200:
        total_sum *= 0.75
    if day_of_month <= 15:
        total_sum *= 0.9

print(f'{total_sum:.2f}')