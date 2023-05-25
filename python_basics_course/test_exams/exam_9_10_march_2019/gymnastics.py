country = input()
game = input()

result = 0

if game == 'ribbon':
    if country == 'Russia':
        result = 9.100 + 9.400
    elif country == 'Bulgaria':
        result = 9.600 + 9.400
    elif country == 'Italy':
        result = 9.200 + 9.500

elif game == 'hoop':
    if country == 'Russia':
        result = 9.300 + 9.800
    elif country == 'Bulgaria':
        result = 9.550 + 9.750
    elif country == 'Italy':
        result = 9.450 + 9.350

elif game == 'rope':
    if country == 'Russia':
        result = 9.600 + 9.000
    elif country == 'Bulgaria':
        result = 9.500 + 9.400
    elif country == 'Italy':
        result = 9.700 + 9.150

left_points = 20 - result
percent_result = left_points / 20 * 100

print(f'The team of {country} get {result:.3f} on {game}.')
print(f'{percent_result:.2f}%')