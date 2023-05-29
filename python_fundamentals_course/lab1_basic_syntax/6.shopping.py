budget = int(input())
price = input()

while price != "End":
    current_price = int(price)
    budget -= current_price
    if budget < 0:
        print('You went in overdraft!')
        exit()
    price = input()

print("You bought everything needed.")