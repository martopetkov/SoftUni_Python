chas_na_izpita = int(input())
minuta_na_izpita = int(input())
chas_na_pristigane = int(input())
min_na_pristigane = int(input())

exam_time_in_min = chas_na_izpita * 60 + minuta_na_izpita
arrival_time_in_min = chas_na_pristigane * 60 + min_na_pristigane

diff = abs(exam_time_in_min - arrival_time_in_min)
hours = diff // 60
minutes = diff % 60

if exam_time_in_min == arrival_time_in_min:
    print('On time')

elif exam_time_in_min > arrival_time_in_min:
    if diff <= 30:
        print('On time')
        print(f'{diff} minutes before the start')
    elif 30 < diff <= 59:
        print('Early')
        print(f'{diff} minutes before the start')
    else:
        print(f'Early')
        print(f'{hours}:{minutes:02d} hours before the start')

elif exam_time_in_min < arrival_time_in_min:
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        print(f'{hours}:{minutes:02d} hours after the start')










