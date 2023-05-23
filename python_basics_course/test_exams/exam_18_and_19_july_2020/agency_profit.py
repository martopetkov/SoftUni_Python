aviocompany = input()
adult_tickets = int(input())
child_tickets = int(input())
net_price_for_adult = float(input())
service_tax = float(input())
profit = 0

net_price_for_child = net_price_for_adult - ((net_price_for_adult * 70) / 100)
total_price = (child_tickets * (net_price_for_child + service_tax)) + (adult_tickets * (net_price_for_adult + service_tax))
profit = total_price * 0.2

print(f'The profit of your agency from {aviocompany} tickets is {profit:.2f} lv.')
