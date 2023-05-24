
food_in_kg = input()
food_in_gr = int(food_in_kg) * 1000
bought_food = 0

while True:
    command = input()
    if command == 'Adopted':
        break
    bought_food += int(command)

diff = abs(food_in_gr - bought_food)
if bought_food <= food_in_gr:
    print(f'Food is enough! Leftovers: {diff} grams.')
else:
    print(f'Food is not enough. You need {diff} grams more.')


