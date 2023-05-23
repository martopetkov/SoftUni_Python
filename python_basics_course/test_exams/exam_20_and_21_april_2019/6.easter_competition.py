from sys import maxsize

max_points = -maxsize
num_bakers = int(input())
best_baker = ''

for k in range(1, num_bakers + 1):
    baker_points = 0
    baker_name = input()
    command = input()
    while command != 'Stop':
        baker_points += int(command)

        command = input()
    print(f'{baker_name} has {baker_points} points.')
    if baker_points > max_points:
        max_points = baker_points
        best_baker = baker_name
        print(f'{best_baker} is the new number 1!')

print(f'{best_baker} won competition with {max_points} points!')

