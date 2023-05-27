num_of_locations = int(input())

for l in range(num_of_locations):
    expected_gold_per_day = float(input())
    num_of_days_per_location = int(input())

    total_gold = 0
    average_gold = 0
    for n in range(num_of_days_per_location):
        gold_per_day = float(input())
        total_gold += gold_per_day
    average_gold = total_gold / num_of_days_per_location

    if average_gold >= expected_gold_per_day:
        print(f'Good job! Average gold per day: {average_gold:.2f}.')
    else:
        print(f'You need {abs(expected_gold_per_day - average_gold):.2f} gold.')
