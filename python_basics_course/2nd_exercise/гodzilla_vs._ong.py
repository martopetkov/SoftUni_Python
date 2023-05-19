budjet = float(input())
statists = int(input())
drehi = float(input())

price_for_decors = budjet * 0.1
if statists > 150:
    drehi = drehi * 0.9
price_for_drehi = statists * drehi
total_movie_cost = price_for_drehi + price_for_decors
diff = abs(budjet - total_movie_cost)

if total_movie_cost > budjet:
    print('Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
