eggs_first_player = int(input())
eggs_second_player = int(input())
winner = input()
is_valid = True

while winner != 'End':
    if winner == 'one':
        eggs_second_player -= 1
    if eggs_second_player == 0:
        print(f'Player two is out of eggs. Player one has {eggs_first_player} eggs left.')
        is_valid = False
        break

    if winner == 'two':
        eggs_first_player -= 1
    if eggs_first_player == 0:
        print(f'Player one is out of eggs. Player two has {eggs_second_player} eggs left.')
        is_valid = False
        break
    winner = input()
if is_valid:
    print(f'Player one has {eggs_first_player} eggs left.')
    print(f'Player two has {eggs_second_player} eggs left.')