broi_hrizantemi = int(input())
broi_rozi = int(input())
broi_laleta = int(input())
season = input()
praznik_li_e = input()

total_price = 0
aranjirane = 0

if season == 'Spring' or season == 'Summer':
    total_price = (broi_hrizantemi * 2) + (broi_rozi * 4.1) + (broi_laleta * 2.5)
elif season == 'Autumn' or season == 'Winter':
    total_price = (broi_hrizantemi * 3.75) + (broi_rozi * 4.5) + (broi_laleta * 4.15)

if praznik_li_e == 'Y':
    total_price *= 1.15
if broi_laleta >= 7 and season == 'Spring':
    total_price *= 0.95
if broi_rozi >= 10 and season == 'Winter':
    total_price *= 0.90
if (broi_rozi + broi_laleta + broi_hrizantemi) >= 20:
    total_price *= 0.8

aranjirane = total_price + 2
print(f'{aranjirane:.2f}')