name_one = input()
name_two = input()
is_valid = True

one_points = 0
two_points = 0

card_one = input()

while card_one != "End of game":
    winner = ''
    card_two = int(input())
    if int(card_one) > card_two:
        one_points += int(card_one) - card_two
    elif int(card_one) < card_two:
        two_points += card_two - int(card_one)
    elif int(card_one) == card_two:
        print('Number wars!')
        card_one = int(input())
        card_two = int(input())
        if card_one > card_two:
            print(f'{name_one} is winner with {card_one - card_two} points')
        elif card_one < card_two:
            print(f'{name_two} is winner with {card_two - card_one} points')
        is_valid = False
        break
    card_one = input()

if is_valid:
    print(f'{name_one} has {one_points} points')
    print(f'{name_two} has {two_points} points')