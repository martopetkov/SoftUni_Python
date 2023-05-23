from math import ceil

guests = int(input())
budjet = int(input())

needed_kozunaci = ceil(guests / 3)
needed_eggs = guests * 2

suma = (needed_kozunaci * 4) + (needed_eggs * 0.45)

diff = abs(budjet - suma)

if budjet >= suma:
    print(f'Lyubo bought {needed_kozunaci} Easter bread and {needed_eggs} eggs.')
    print(f'He has {diff:.2f} lv. left.')
else:
    print("Lyubo doesn't have enough money.")
    print(f'He needs {diff:.2f} lv. more.')