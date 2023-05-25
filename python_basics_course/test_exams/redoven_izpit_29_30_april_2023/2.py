from math import floor

shirina = float(input())
daljina = float(input())
visochina = float(input())
average_man_height = float(input())

rocket_volume = shirina * daljina * visochina
room_volume = (average_man_height + 0.4) * 2 * 2
total_space = floor(rocket_volume / room_volume)

if total_space < 3:
    print('The spacecraft is too small.')
elif total_space > 10:
    print('The spacecraft is too big.')
else:
    print(f'The spacecraft holds {total_space} astronauts.')