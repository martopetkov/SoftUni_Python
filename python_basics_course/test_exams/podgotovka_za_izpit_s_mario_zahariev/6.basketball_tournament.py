wins = 0
losses = 0

tournament_name = input()
total_games = 0

while tournament_name != "End of tournaments":
    num_of_games = int(input())
    games = 0
    for t in range(1, num_of_games +1):
        desi_team_points = int(input())
        second_team_points = int(input())
        diff = abs(desi_team_points - second_team_points)
        games += 1
        if desi_team_points > second_team_points:
            wins += 1
            print(f'Game {games} of tournament {tournament_name}: win with {diff} points.')
        else:
            losses += 1
            print(f'Game {games} of tournament {tournament_name}: lost with {diff} points.')
    total_games += games
    tournament_name = input()

print(f'{((wins / total_games) * 100):.2f}% matches win')
print(f'{((losses / total_games) * 100):.2f}% matches lost')