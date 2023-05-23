clients = int(input())
average_money = 0


for i in range(1, clients + 1):
    product = input()
    money = 0
    items = 0
    while product != "Finish":

        if product == 'basket':
            money += 1.5
            items += 1
        elif product == 'wreath':
            money += 3.8
            items += 1
        elif product == 'chocolate bunny':
            money += 7
            items += 1

        product = input()

    if items % 2 == 0:
        money *= 0.8
    average_money += money
    print(f'You purchased {items} items for {money:.2f} leva.')


print(f'Average bill per client is: {(average_money / clients):.2f} leva.')