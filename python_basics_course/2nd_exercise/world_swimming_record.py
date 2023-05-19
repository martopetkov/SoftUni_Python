from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

needs_to_swim_in_seconds = distance_in_meters * time_in_seconds_for_one_meter
extra_time = floor(distance_in_meters / 15) * 12.5
total_time = (needs_to_swim_in_seconds + extra_time)

diff = abs(record_in_seconds - total_time)
if total_time < record_in_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {diff:.2f} seconds slower.')