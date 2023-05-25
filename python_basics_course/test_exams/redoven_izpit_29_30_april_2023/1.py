from math import ceil

average_speed = float(input())
needed_fuel = float(input())

total_distance = 384400 * 2
needed_time = ceil(total_distance / average_speed)
total_time = needed_time + 3
needed_fuel = (needed_fuel * total_distance) / 100

print(f'{total_time}')
print(f'{needed_fuel:.0f}')