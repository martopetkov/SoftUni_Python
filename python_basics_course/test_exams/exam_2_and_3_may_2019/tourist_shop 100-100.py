num_of_products = 0
price_of_products = 0

is_valid = True
budjet = float(input())
product = input()
while product != 'Stop':
    product_price = float(input())

    num_of_products += 1
    if num_of_products % 3 == 0:
        product_price *= 0.5
    price_of_products += product_price

    if product_price <= budjet:
        budjet -= product_price
    else:
        print("You don't have enough money!")
        print(f'You need {(abs(product_price-budjet)):.2f} leva!')
        is_valid = False
        break

    product = input()

if is_valid:
    print(f'You bought {num_of_products} products for {price_of_products:.2f} leva.')