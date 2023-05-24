number_of_days = int(input())
total_food = float(input())

count_days = 0
biscuits = 0
food_ate_by_dog = 0
food_ate_by_cat = 0
all_biscuits = 0

for days in range(1, number_of_days + 1):
    food_for_dog = int(input())
    food_ate_by_dog += food_for_dog
    food_for_cat = int(input())
    food_ate_by_cat += food_for_cat
    count_days += 1
    if count_days % 3 == 0:
        biscuits = (food_for_dog + food_for_cat) * 0.1
        all_biscuits += biscuits

ate_food = food_ate_by_dog + food_ate_by_cat
average_food = (ate_food * 100) / total_food
average_food_by_dog = (food_ate_by_dog * 100) / ate_food
average_food_by_cat = (food_ate_by_cat * 100) / ate_food

print(f'Total eaten biscuits: {round(all_biscuits)}gr.')
print(f'{average_food:.2f}% of the food has been eaten.')
print(f'{average_food_by_dog:.2f}% eaten from the dog.')
print(f'{average_food_by_cat:.2f}% eaten from the cat.')
