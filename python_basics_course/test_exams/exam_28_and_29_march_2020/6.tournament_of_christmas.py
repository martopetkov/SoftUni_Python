tournament_days = int(input())

won_game = 0
lost_game = 0
won_sum = 0
lost_sum = 0
money_for_the_day = 0
bonus_for_the_day = 0
all_money = 0

while True:
    game = input()
    if game == 'Finish':
        money_for_the_day = won_sum - lost_sum
        if won_game > lost_game:
            bonus_for_the_day = money_for_the_day * 0.1
        if lost_game == 0:
            bonus_for_the_day = money_for_the_day * 0.2
        all_money = money_for_the_day + bonus_for_the_day
        break
    result = input()
    if result == 'win':
        won_sum += 20
        won_game += 1
    elif result == 'lose':
        lost_sum += 0
        lost_game += 1
if won_game > lost_game:
    print(f'You won the tournament! Total raised money: {all_money:.2f}')
else:
    print(f'You won the tournament! Total raised money: {all_money:.2f}')
