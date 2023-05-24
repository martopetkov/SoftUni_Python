contract_period = input()
type_of_contract = input()
added_net = input()
months = int(input())

price_per_month = 0
net_price = 0

if contract_period == 'one':
    if type_of_contract == 'Small':
        price_per_month = 9.98
    elif type_of_contract == 'Middle':
        price_per_month = 18.99
    elif type_of_contract == 'Large':
        price_per_month = 25.98
    elif type_of_contract == 'ExtraLarge':
        price_per_month = 35.99

elif contract_period == 'two':
    if type_of_contract == 'Small':
        price_per_month = 8.58
    elif type_of_contract == 'Middle':
        price_per_month = 17.09
    elif type_of_contract == 'Large':
        price_per_month = 23.59
    elif type_of_contract == 'ExtraLarge':
        price_per_month = 31.79

if added_net == 'yes':
    if price_per_month <= 10:
        net_price = 5.50
    elif 10 < price_per_month <= 30:
        net_price = 4.35
    elif price_per_month > 30:
        net_price = 3.85

total_price = (price_per_month + net_price) * months
if contract_period == 'two':
    total_price = total_price - ((total_price * 3.75) / 100)

print(f'{total_price:.2f} lv.')