game_moves = int(input())
total_points = 0

range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0
range6 = 0

for i in range(game_moves):
    chislo = int(input())
    if 0 <= chislo <= 9:
        total_points = total_points + chislo * 0.2
        range1 +=1
    elif 10 <= chislo <= 19:
        total_points = total_points + chislo * 0.3
        range2 += 1
    elif 20 <= chislo <= 29:
        total_points = total_points + chislo * 0.4
        range3 += 1
    elif 30 <= chislo <= 39:
        total_points += 50
        range4 += 1
    elif 40 <= chislo <= 50:
        total_points += 100
        range5 += 1
    elif 51 <= chislo:
        total_points = total_points / 2
        range6 += 1
    elif chislo < 0:
        total_points = total_points / 2
        range6 += 1

procent_range1 = range1 / game_moves * 100
procent_range2 = range2 / game_moves * 100
procent_range3 = range3 / game_moves * 100
procent_range4 = range4 / game_moves * 100
procent_range5 = range5 / game_moves * 100
procent_range6 = range6 / game_moves * 100

print(f'{total_points:.2f}')
print(f'From 0 to 9: {procent_range1:.2f}%')
print(f'From 10 to 19: {procent_range2:.2f}%')
print(f'From 20 to 29: {procent_range3:.2f}%')
print(f'From 30 to 39: {procent_range4:.2f}%')
print(f'From 40 to 50: {procent_range5:.2f}%')
print(f'Invalid numbers: {procent_range6:.2f}%')
