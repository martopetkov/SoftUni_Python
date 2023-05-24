fruit = input()
package_size = input()
number_of_sets = int(input())
price = 0
discount = 0

if fruit == 'Watermelon':
    if package_size == 'small':
        price = 2 * 56
    elif package_size == 'big':
        price = 5 * 28.70
elif fruit == 'Mango':
    if package_size == 'small':
        price = 2 * 36.66
    elif package_size == 'big':
        price = 5 * 19.60
elif fruit == 'Pineapple':
    if package_size == 'small':
        price = 2 * 42.10
    elif package_size == 'big':
        price = 5 * 24.80
elif fruit == 'Raspberry':
    if package_size == 'small':
        price = 2 * 20
    elif package_size == 'big':
        price = 5 * 15.20

price_for_sets = price * number_of_sets
if 400 <= price_for_sets <= 1000:
    discount = price_for_sets * 0.15
elif price_for_sets > 1000:
    discount = price_for_sets * 0.5

total_price = price_for_sets - discount

print(f'{(total_price):.2f} lv.')

