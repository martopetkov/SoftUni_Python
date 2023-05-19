hours = int(input())
minutes = int(input())

total_time_in_minutes = hours * 60 + minutes + 15

total_hours = total_time_in_minutes // 60
total_minutes = total_time_in_minutes % 60

if total_hours > 23:
    total_hours = 0
if total_minutes > 59:
    total_minutes = 0

if total_minutes < 10:
    print(f'{total_hours}:0{total_minutes}')

else:
    print(f'{total_hours}:{total_minutes}')