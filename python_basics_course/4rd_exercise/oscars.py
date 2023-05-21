name = input()
start_points = float(input())
jury = int(input())

total_points = 0

for i in range(jury):
    jury_name = input()
    jury_points = float(input())
    total_points = start_points + ((len(jury_name) * jury_points) / 2)
    start_points = total_points
    if start_points >= 1250.5:
        break

needed_points = 1250.5 - total_points

if total_points >= 1250.5:
    print(f'Congratulations, {name} got a nominee for leading role with {total_points:.1f}!')
else:
    print(f'Sorry, {name} you need {needed_points:.1f} more!')