from math import ceil, floor

tennis_rocket_price = float(input())
num_tennis_rockets = int(input())
num_shoes = int(input())

rocket_price = num_tennis_rockets * tennis_rocket_price
shoes_price = tennis_rocket_price / 6
all_shoes_price = num_shoes * shoes_price
rest_equipment = (rocket_price + all_shoes_price) * 0.2
total_sum = rocket_price + all_shoes_price + rest_equipment

sum_by_Djokovic = total_sum / 8
rest_of_the_sum = total_sum * 7 / 8

print(f'Price to be paid by Djokovic {floor(sum_by_Djokovic)}')
print(f'Price to be paid by sponsors {ceil(rest_of_the_sum)}')