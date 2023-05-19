season = input()
km_per_month = float(input())
zaplata = 0

if season == 'Spring' or season == 'Autumn':
    if km_per_month <= 5000:
        zaplata = km_per_month * 0.75 * 4
    elif 5000 < km_per_month <= 10000:
        zaplata = km_per_month * 0.95 * 4
    elif 10000 < km_per_month <= 20000:
        zaplata = km_per_month * 1.45 * 4
elif season == 'Summer':
    if km_per_month <= 5000:
        zaplata = km_per_month * 0.9 * 4
    elif 5000 < km_per_month <= 10000:
        zaplata = km_per_month * 1.1 * 4
    elif 10000 < km_per_month <= 20000:
        zaplata = km_per_month * 1.45 * 4
elif season == 'Winter':
    if km_per_month <= 5000:
        zaplata = km_per_month * 1.05 * 4
    elif 5000 < km_per_month <= 10000:
        zaplata = (km_per_month * 1.25) * 4
    elif 10000 < km_per_month <= 20000:
        zaplata = km_per_month * 1.45 * 4

after_taxes = zaplata * 0.9

print(f'{after_taxes:.2f}')