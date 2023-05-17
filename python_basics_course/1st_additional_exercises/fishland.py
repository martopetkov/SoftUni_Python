skumria_per_kg = float(input())
caca_per_kg = float(input())
palamud_kilos = float(input())
safrid_kilos = float(input())
midi_kilos = int(input())

palamud_price = skumria_per_kg + skumria_per_kg * 0.6
sum_palamud = palamud_price * palamud_kilos
safrid_price = caca_per_kg + caca_per_kg * 0.8
sum_safrid = safrid_price * safrid_kilos
midi_price = midi_kilos * 7.50

total_price = sum_palamud + sum_safrid + midi_price
print(f'{total_price:.2f}')