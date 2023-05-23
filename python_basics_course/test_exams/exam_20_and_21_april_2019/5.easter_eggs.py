from sys import maxsize
painter_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

max_number = -maxsize
best_color = ''

for i in range(1, painter_eggs + 1):
    egg_color = input()

    if egg_color == 'red':
        red_eggs += 1
        if red_eggs > max_number:
            max_number = red_eggs
            best_color = 'red'

    elif egg_color == 'orange':
        orange_eggs += 1
        if orange_eggs > max_number:
            max_number = orange_eggs
            best_color = 'orange'

    elif egg_color == 'blue':
        blue_eggs += 1
        if blue_eggs > max_number:
            max_number = blue_eggs
            best_color = 'blue'

    elif egg_color == 'green':
        green_eggs += 1
        if green_eggs > max_number:
            max_number = green_eggs
            best_color = 'green'

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_number} -> {best_color}')