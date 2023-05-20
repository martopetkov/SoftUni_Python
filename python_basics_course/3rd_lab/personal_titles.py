godini = float(input())
pol = input()

if pol == 'm':
    if godini < 16:
        print('Master')
    else:
        print('Mr.')
elif pol == 'f':
    if godini < 16:
        print('Miss')
    else:
        print(f'Ms.')