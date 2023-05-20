chas = int(input())
den = input()

if den == 'Monday' or den == 'Tuesday' or den == 'Wednesday' or den == 'Thursday' or den == 'Friday' or den == 'Saturday':
    if 10 <= chas <= 18:
        print('open')
    else:
        print('closed')

elif den == 'Sunday':
    print('closed')