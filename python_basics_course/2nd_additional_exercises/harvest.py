from math import ceil
from math import floor


loze_kv_m = int(input())
grozde_za_kv_m = float(input())
needed_liters = int(input())
number_of_robi = int(input())

obshto_grozde = loze_kv_m * grozde_za_kv_m
za_vino = ceil((obshto_grozde * 0.4) / 2.5)
diff = floor(abs(needed_liters - za_vino))
leftovers = floor(abs(za_vino - needed_liters))
per_man = ceil(leftovers / number_of_robi)

if za_vino < needed_liters:
    print(f'It will be a tough winter! More {leftovers:.0f} liters wine needed.')
elif za_vino >= needed_liters:
    print(f'Good harvest this year! Total wine: {za_vino:.0f} liters.')
    print(f'{leftovers:.0f} liters left -> {per_man:.0f} liters per person.')


