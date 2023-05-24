capacity = float(input())

num_of_loads = 1

while True:
    command = input()
    if command == "End":
        print('Congratulations! All suitcases are loaded!')
        break

    volume = float(command)
    if num_of_loads % 3 == 0:
        volume += (10 / 100) * volume
    if capacity < volume or capacity <= 0:
        print('No more space!')
        break
    else:
        num_of_loads += 1
    capacity -= volume

print(f'Statistic: {num_of_loads - 1} suitcases loaded.')

