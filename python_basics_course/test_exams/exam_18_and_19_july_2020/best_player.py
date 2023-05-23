from sys import maxsize

maxsize = -maxsize
goals_num = 0
hattricks = 0

while True:
    player_name = input()
    if player_name == 'END':
        break
    goals_num = int(input())

    if goals_num > maxsize:
        maxsize = goals_num
        best_player = player_name
    if goals_num >= 3:
        hattricks += 1

print(f'{best_player} is the best player!')
if goals_num >= 3:
    print(f'He has scored {goals_num} goals and made a hat-trick !!!')
else:
    print(f'He has scored {goals_num} goals.')