num_of_days = int(input())
hours = int(input())
price = 0
day = 0
total_price = 0

for d in range(1, num_of_days + 1):
    price = 0
    for h in range(1, hours + 1):
        if d % 2 == 0 and h % 2 != 0:
            price += 2.5
        elif d % 2 != 0 and h % 2 == 0:
            price += 1.25
        else:
            price += 1
    day += 1
    total_price += price

    print(f'Day: {day} - {price:.2f} leva')

print(f'Total: {total_price:.2f} leva')
