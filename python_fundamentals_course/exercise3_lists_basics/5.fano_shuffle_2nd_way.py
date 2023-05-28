cards = input().split()
faro_counter = int(input())

for shuffle in range(faro_counter):
    deck = []
    middle_of_deck = len(cards) // 2
    left_part = cards[0:middle_of_deck]
    right_part = cards[middle_of_deck::]

    for card in range(len(left_part)):
        deck.append(left_part[card])
        deck.append(right_part[card])
    cards = deck

print(cards)