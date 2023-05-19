from math import ceil

number_of_days = int(input())
left_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

needed_dog_food = number_of_days * dog_food_per_day
needed_cat_food = number_of_days * cat_food_per_day
needed_turtle_food = (number_of_days * turtle_food_per_day) / 1000

total_needed_food = ceil(needed_dog_food + needed_cat_food + needed_turtle_food)
diff = ceil(abs(left_food - total_needed_food))
if total_needed_food < left_food:
    print(f"{diff} kilos of food left.")
else:
    print(f"{diff} more kilos of food are needed.")