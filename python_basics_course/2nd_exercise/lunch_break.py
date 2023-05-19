from math import ceil

tv_series_name = input()
episode_length = int(input())
break_length = int(input())

lunch_break_time = break_length * 1 / 8
relax_time = break_length * 1 / 4
left_time = (break_length - lunch_break_time - relax_time)

diff = abs(episode_length - left_time)
if episode_length <= left_time:
    print(f'You have enough time to watch {tv_series_name} and left with {ceil(diff)} minutes free time.')
else:
    print(f"You don't have enough time to watch {tv_series_name}, you need {ceil(diff)} more minutes.")
