from math import floor
num_of_balls = int(input())

points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_color_balls = 0
divides_black_ball = 0

for _ in range(num_of_balls):
    color = input()
    if color == 'red':
        points += 5
        red_balls += 1
    elif color == 'orange':
        points += 10
        orange_balls += 1
    elif color == 'yellow':
        points += 15
        yellow_balls += 1
    elif color == 'white':
        points += 20
        white_balls += 1
    elif color == 'black':
        points = floor(points / 2)
        divides_black_ball +=1
    else:
        other_color_balls += 1

print(f'Total points: {points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_color_balls}')
print(f'Divides from black balls: {divides_black_ball}')