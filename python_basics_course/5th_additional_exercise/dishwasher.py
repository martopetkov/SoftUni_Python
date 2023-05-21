bottles = int(input())

preparat = bottles * 750
chisti_chinii = 0
chisti_tendjeri = 0
count = 0
sum_chinii = 0
sum_tendjeri = 0

while preparat >= 0:
    count += 1
    command = input()
    if command == 'End':
        break

    if count % 3 == 0:
        chisti_tendjeri = int(command)
        sum_tendjeri += chisti_tendjeri
        preparat = preparat - (chisti_tendjeri * 15)

    else:
        chisti_chinii = int(command)
        sum_chinii += chisti_chinii
        preparat = preparat - (chisti_chinii * 5)

if preparat < 0:
    print(f'Not enough detergent, {abs(preparat)} ml. more necessary!')

else:
    print('Detergent was enough!')
    print(f'{sum_chinii} dishes and {sum_tendjeri} pots were washed.')
    print(f'Leftover detergent {preparat} ml.')
