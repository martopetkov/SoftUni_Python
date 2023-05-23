trip_price = float(input())
available_money = float(input())

spend_days = 0
saved_days = 0

while True:
    saved_days += 1
    action = input()
    new_sum = float(input())

    if action == 'spend':
        spend_days += 1
        available_money -= new_sum
        if available_money < 0:
            available_money = 0
    elif action == 'save':
        spend_days = 0
        available_money += new_sum

    if available_money >= trip_price:
        print(f'You saved the money for {saved_days} days.')
        break
    elif spend_days >= 5:
        print("You can't save the money.")
        print(saved_days)
        break