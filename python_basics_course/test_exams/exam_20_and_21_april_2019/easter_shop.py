eggs_in_store = int(input())
sold_eggs = 0
command = ''

is_closed = True

while command != 'Close':
    command = input()
    if command == 'Close':
        is_closed = True
        break
    eggs = int(input())

    if command == 'Fill':
        eggs_in_store += eggs
        is_closed = False

    if command == 'Buy':
        if eggs_in_store >= eggs:
            eggs_in_store -= eggs
            sold_eggs += eggs
            is_closed = False
        else:
            print('Not enough eggs in store!')
            print(f'You can buy only {eggs_in_store}.')
            is_closed = False
            break

if is_closed:
    print(f'Store is closed!')
    print(f'{sold_eggs} eggs sold.')