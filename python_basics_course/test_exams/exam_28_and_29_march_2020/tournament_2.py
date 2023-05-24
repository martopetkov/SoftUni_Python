tournament_days = int(input())

won_sum = 0
wins = 0
lost = 0
total_won_sum = 0
days_won = 0
days_lost = 0

for days in range(1, tournament_days + 1):

    won_sum = 0
    wins = 0
    lost = 0
    sport = input()

    while sport != 'Finish':

        result = input()
        if result == 'win':
            won_sum += 20
            wins += 1
        elif result == 'lose':
            lost += 1
        sport = input()
    if wins > lost:
        won_sum = won_sum + (won_sum * 0.1)
        days_won += 1

    else:
        days_lost += 1
    total_won_sum += won_sum

if days_won > days_lost:
    total_won_sum = total_won_sum + (total_won_sum * 0.2)
    print(f'You won the tournament! Total raised money: {total_won_sum:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_won_sum:.2f}')