num_dogrami = int(input())
type_dogrami = input()
shipping_method = input()

discount = 0

if type_dogrami == '90X130':
    discount = num_dogrami * 110
    if 30 < num_dogrami <= 60:
        discount *= 0.95
    elif num_dogrami > 60:
        discount *= 0.92

elif type_dogrami == '100X150':
    discount = num_dogrami * 140
    if 40 < num_dogrami <= 80:
        discount *= 0.94
    elif num_dogrami > 80:
        discount *= 0.9

elif type_dogrami == '130X180':
    discount = num_dogrami * 190
    if 20 < num_dogrami <= 50:
        discount *= 0.93
    elif num_dogrami > 50:
        discount *= 0.88

elif type_dogrami == '200X300':
    discount = num_dogrami * 250
    if 25 < num_dogrami <= 50:
        discount *= 0.91
    elif num_dogrami > 50:
        discount *= 0.86

if shipping_method == 'With delivery':
    discount += 60

if num_dogrami > 99:
    discount *= 0.96

if num_dogrami < 10:
    print('Invalid order')
else:
    print(f'{discount:.2f} BGN')