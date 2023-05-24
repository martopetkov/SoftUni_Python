walking_minutes_per_day = int(input())
number_of_walks_per_day = int(input())
gained_calories_per_day = int(input())

total_minutes_per_day = walking_minutes_per_day * number_of_walks_per_day
total_burned_calories = total_minutes_per_day * 5
fifty_percent_calories = gained_calories_per_day / 2

if total_burned_calories >= fifty_percent_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.')