def price(food, number):
    dollars = 0
    if product == "coffee":
        dollars = quantity * 1.5
    elif product == "water":
        dollars = quantity * 1
    elif product == "coke":
        dollars = quantity * 1.4
    elif product == "snacks":
        dollars = quantity * 2
    return dollars


product = input()
quantity = int(input())


cost = price(product, quantity)
print(f"{cost:.2f}")