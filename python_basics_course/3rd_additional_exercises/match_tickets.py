budjet = float(input())
ticket_type = input()
number_of_people = int(input())

total_ticket_price = 0
transport = 0
razhodi = 0

if ticket_type == 'Normal':
    total_ticket_price = number_of_people * 249.99
elif ticket_type == 'VIP':
    total_ticket_price = number_of_people * 499.99

if 1 <= number_of_people <= 4:
    transport = budjet * 0.75
elif 5 <= number_of_people <= 9:
    transport = budjet * 0.60
elif 10 <= number_of_people <= 24:
    transport = budjet * 0.50
elif 25 <= number_of_people <= 49:
    transport = budjet * 0.4
elif number_of_people > 50:
    transport = budjet * 0.25

razhodi = transport + total_ticket_price
diff = abs(budjet - razhodi)

if budjet >= razhodi:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')