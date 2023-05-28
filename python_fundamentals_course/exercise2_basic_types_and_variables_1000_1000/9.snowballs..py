snowball_num = int(input())
highest_value = float('-inf')
best_ball = ''

for s in range(snowball_num):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    value = (snowball_weight / snowball_time) ** snowball_quality

    if value > highest_value:
        highest_value = value
        best_ball = f'{snowball_weight} : {snowball_time} = {value:.0f} ({snowball_quality})'

print(best_ball)