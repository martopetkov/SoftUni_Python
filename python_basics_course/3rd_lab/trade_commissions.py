grad = input()
prodajbi = float(input())
komisionna = 0

FALSE_DATA = False

if grad == 'Sofia':
        if 0 <= prodajbi <= 500:
            komisionna = 0.05
        elif 500 < prodajbi <= 1000:
            komisionna = 0.07
        elif 1000 < prodajbi <= 10000:
            komisionna = 0.08
        elif prodajbi > 10000:
            komisionna = 0.12
        else:
            FALSE_DATA = True

elif grad == 'Varna':
        if 0 <= prodajbi <= 500:
            komisionna = 0.045
        elif 500 < prodajbi <= 1000:
            komisionna = 0.075
        elif 1000 < prodajbi <= 10000:
            komisionna = 0.1
        elif prodajbi > 10000:
            komisionna = 0.13
        else:
            FALSE_DATA = True
elif grad == 'Plovdiv':
        if 0 <= prodajbi <= 500:
            komisionna = 0.055
        elif 500 < prodajbi <= 1000:
            komisionna = 0.08
        elif 1000 < prodajbi <= 10000:
            komisionna = 0.12
        elif prodajbi > 10000:
            komisionna = 0.145
        else:
            FALSE_DATA = True
else:
    FALSE_DATA = True

if not FALSE_DATA:
    print(f'{prodajbi * komisionna:.2f}')
else:
    print('error')


