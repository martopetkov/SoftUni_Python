egg_size = input()
egg_color = input()
portion_num = int(input())

price = 0

if egg_size == "Large":
    if egg_color == 'Red':
        price = 16
    elif egg_color == 'Green':
        price = 12
    elif egg_color == 'Yellow':
        price = 9

elif egg_size == "Medium":
    if egg_color == 'Red':
        price = 13
    elif egg_color == 'Green':
        price = 9
    elif egg_color == 'Yellow':
        price = 7

elif egg_size == "Small":
    if egg_color == 'Red':
        price = 9
    elif egg_color == 'Green':
        price = 8
    elif egg_color == 'Yellow':
        price = 5

egg_price = price * portion_num
razhodi = egg_price * 0.35

print(f'{egg_price - razhodi:.2f} leva.')