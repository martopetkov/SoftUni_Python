meseci = int(input())

total_electricity = 0
total_water = 0
total_internet = 0
total_other = 0

for i in range(meseci):
    smetka_za_tok = float(input())
    total_electricity += smetka_za_tok
    total_water += 20
    total_internet += 15
    total_other += (smetka_za_tok + 20 + 15) * 0.2 + (smetka_za_tok + 20 + 15)

average = (total_electricity + total_water + total_internet + total_other) / meseci

print(f'Electricity: {total_electricity:.2f} lv')
print(f'Water: {total_water:.2f} lv')
print(f'Internet: {total_internet:.2f} lv')
print(f'Other: {total_other:.2f} lv')
print(f'Average: {average:.2f} lv')