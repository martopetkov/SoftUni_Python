from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_one_meter = float(input())

needs_to_climb = distance_in_meters * time_in_seconds_per_one_meter
extra_time = floor(distance_in_meters / 50) * 30
total_time = needs_to_climb + extra_time

diff = abs(total_time - record_in_seconds)
if total_time < record_in_seconds:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {diff:.2f} seconds slower.')