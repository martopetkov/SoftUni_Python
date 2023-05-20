plod = input()
den = input()
kolichestvo = float(input())
cena = 0

FALSE_DATA = False

if den == 'Monday' or den == 'Tuesday' or den == 'Wednesday' or den == 'Thursday' or den == 'Friday':
    if plod == 'banana':
        cena = kolichestvo * 2.5
    elif plod == 'apple':
        cena = kolichestvo * 1.2
    elif plod == 'orange':
        cena = kolichestvo * 0.85
    elif plod == 'grapefruit':
        cena = kolichestvo * 1.45
    elif plod == 'kiwi':
        cena = kolichestvo * 2.7
    elif plod == 'pineapple':
        cena = kolichestvo * 5.5
    elif plod == 'grapes':
        cena = kolichestvo * 3.85
    else:
        FALSE_DATA = True

elif den == 'Saturday' or den == 'Sunday':
    if plod == 'banana':
        cena = kolichestvo * 2.7
    elif plod == 'apple':
        cena = kolichestvo * 1.25
    elif plod == 'orange':
        cena = kolichestvo * 0.9
    elif plod == 'grapefruit':
        cena = kolichestvo * 1.6
    elif plod == 'kiwi':
        cena = kolichestvo * 3
    elif plod == 'pineapple':
        cena = kolichestvo * 5.6
    elif plod == 'grapes':
        cena = kolichestvo * 4.2
    else:
        FALSE_DATA = True
else:
    FALSE_DATA = True

if not FALSE_DATA:
    print(f'{cena:.2f}')
else:
    print('error')