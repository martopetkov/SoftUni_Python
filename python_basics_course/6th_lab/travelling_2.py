money = 0
destination = ''

while destination != "End":
    destination = input()
    if destination == "End":
        break
    price = float(input())
    money = 0
    while price > money:
        current_money = float(input())
        money += current_money
    print(f"Going to {destination}!")