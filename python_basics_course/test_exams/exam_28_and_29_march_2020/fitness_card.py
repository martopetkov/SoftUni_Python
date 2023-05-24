available_sum = float(input())
gender = input()
age = int(input())
sport = input()

sum_card = 0

if sport == 'Gym':
    if gender == 'm':
        sum_card = 42
    elif gender == 'f':
        sum_card = 35
elif sport == 'Boxing':
    if gender == 'm':
        sum_card = 41
    elif gender == 'f':
        sum_card = 37
elif sport == 'Yoga':
    if gender == 'm':
        sum_card = 45
    elif gender == 'f':
        sum_card = 42
elif sport == 'Zumba':
    if gender == 'm':
        sum_card = 34
    elif gender == 'f':
        sum_card = 31
elif sport == 'Dances':
    if gender == 'm':
        sum_card = 51
    elif gender == 'f':
        sum_card = 53
elif sport == 'Pilates':
    if gender == 'm':
        sum_card = 39
    elif gender == 'f':
        sum_card = 37

if age <= 19:
    discount = sum_card * 0.2
    sum_card -= discount

if sum_card <= available_sum:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f"You don't have enough money! You need ${(sum_card - available_sum):.2f} more.")