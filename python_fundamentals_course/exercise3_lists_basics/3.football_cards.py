cards = input().split()

first_team_sent_off_players = []
second_team_sent_off_players = []
should_terminate = False

for card in cards:
    if card in first_team_sent_off_players or card in second_team_sent_off_players:
        # така ще игнорираме ако някой картон (карта) се повтаря повече от веднъж
        continue
    card_args = card.split("-")  #разделя всяка карта без тиренце
    team_name = card_args[0]
    team_number = card_args[1]

    is_first_team = team_name == "A" # реално е булеан, който казва True ако е А и False ако е В
    if is_first_team:
        first_team_sent_off_players.append(card)
    else:
        second_team_sent_off_players.append(card)

    if len(first_team_sent_off_players) > 4 or len(second_team_sent_off_players) > 4:
        should_terminate = True
        break

initial_player_count = 11
first_team_final_player = initial_player_count - len(first_team_sent_off_players)
second_team_final_player = initial_player_count - len(second_team_sent_off_players)

print(f"Team A - {first_team_final_player}; Team B - {second_team_final_player}")

if should_terminate:
    print("Game was terminated")