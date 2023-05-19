season = input()
group_type = input()
number_of_students = int(input())
number_of_nights = int(input())

sport = ''
price = 0

if season == 'Winter':
    if group_type == 'boys' or group_type == 'girls':
        price = number_of_nights * number_of_students * 9.6
    elif group_type == 'mixed':
        price = number_of_nights * number_of_students * 10
elif season == 'Spring':
    if group_type == 'boys' or group_type == 'girls':
        price = number_of_nights * number_of_students * 7.2
    elif group_type == 'mixed':
        price = number_of_nights * number_of_students * 9.5
elif season == 'Summer':
    if group_type == 'boys' or group_type == 'girls':
        price = number_of_nights * number_of_students * 15
    elif group_type == 'mixed':
        price = number_of_nights * number_of_students * 20

if number_of_students >= 50:
    price *= 0.5
elif  20 <= number_of_students < 50:
    price *= 0.85
elif 10 <= number_of_students < 20:
    price *= 0.95

if season == 'Winter':
    if group_type == 'boys':
        sport = 'Judo'
    elif group_type == 'girls':
        sport = 'Gymnastics'
    elif group_type == 'mixed':
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'boys':
        sport = 'Tennis'
    elif group_type == 'girls':
        sport = 'Athletics'
    elif group_type == 'mixed':
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys':
        sport = 'Football'
    elif group_type == 'girls':
        sport = 'Volleyball'
    elif group_type == 'mixed':
        sport = 'Swimming'

print(f'{sport} {price:.2f} lv.')