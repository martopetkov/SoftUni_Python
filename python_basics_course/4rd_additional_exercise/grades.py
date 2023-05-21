broi_studenti = int(input())

dvoika = 0
troika = 0
chetvorka = 0
petica = 0
obshta_ocenka = 0

for i in range(broi_studenti):
    ocenka = float(input())
    obshta_ocenka += ocenka
    if 2.00 <= ocenka <= 2.99:
        dvoika += 1
    elif 3.00 <= ocenka <= 3.99:
        troika += 1
    elif 4.00 <= ocenka <= 4.99:
        chetvorka += 1
    elif 5.00 <= ocenka <= 6.00:
        petica += 1


procenti_petica = petica / broi_studenti * 100
procenti_chetvorka = chetvorka / broi_studenti * 100
procenti_troika = troika / broi_studenti * 100
procenti_dvoika = dvoika / broi_studenti * 100

average = obshta_ocenka / broi_studenti

print(f'Top students: {procenti_petica:.2f}%')
print(f'Between 4.00 and 4.99: {procenti_chetvorka:.2f}%')
print(f'Between 3.00 and 3.99: {procenti_troika:.2f}%')
print(f'Fail: {procenti_dvoika:.2f}%')
print(f'Average: {average:.2f}')