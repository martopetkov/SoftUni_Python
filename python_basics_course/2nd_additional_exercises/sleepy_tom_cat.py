rest_days = int(input())
total_days = 365
norma = 30000
work_days = total_days - rest_days
play_in_rest_days = rest_days * 127
play_in_work_days = (total_days - rest_days) * 63
total_play_in_minutes = play_in_work_days + play_in_rest_days
diff = abs(total_play_in_minutes - norma)
hours = diff // 60
minutes = diff % 60

if total_play_in_minutes >= norma:
    print(f'Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')