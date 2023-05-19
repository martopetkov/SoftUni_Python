broi_kilometri = int(input())
den_ili_nosht = str(input())

taxi_dnevna_tarifa = 0.70 + broi_kilometri * 0.79
taxi_noshtna_tarifa = 0.70 + broi_kilometri * 0.90
bus_tarifa = broi_kilometri * 0.09
train_tarifa = broi_kilometri * 0.06

if broi_kilometri < 20:

    if den_ili_nosht == 'day':
        print(f"{taxi_dnevna_tarifa:.2f}")
    elif den_ili_nosht == 'night':
        print(f"{taxi_noshtna_tarifa:.2f}")

elif 20 <= broi_kilometri < 100:
    if den_ili_nosht == 'day':
        print(f"{bus_tarifa:.2f}")
    elif den_ili_nosht == 'night':
        print(f"{bus_tarifa:.2f}")

elif broi_kilometri >= 100:
    if den_ili_nosht == 'day':
        print(f"{train_tarifa:.2f}")
    elif den_ili_nosht == 'night':
        print(f"{train_tarifa:.2f}")