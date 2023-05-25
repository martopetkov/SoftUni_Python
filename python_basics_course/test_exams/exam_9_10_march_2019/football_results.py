first_game_result = input()
second_game_result = input()
third_game_resulst = input()

wins = 0
draws = 0
lose = 0

text1 = first_game_result
if int(text1[0]) > int(text1[2]):
    wins += 1
elif int(text1[0]) == int(text1[2]):
    draws += 1
elif int(text1[0]) < int(text1[2]):
    lose += 1

text2 = second_game_result
if int(text2[0]) > int(text2[2]):
    wins += 1
elif int(text2[0]) == int(text2[2]):
    draws += 1
elif int(text2[0]) < int(text2[2]):
    lose += 1

text3 = third_game_resulst
if int(text3[0]) > int(text3[2]):
    wins += 1
elif int(text3[0]) == int(text3[2]):
    draws += 1
elif int(text3[0]) < int(text3[2]):
    lose += 1


print(f'Team won {wins} games.')
print(f'Team lost {lose} games.')
print(f'Drawn games: {draws}')