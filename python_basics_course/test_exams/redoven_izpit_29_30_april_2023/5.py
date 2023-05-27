command = input()

kids = 0
adults = 0
toys = 0
sweaters = 0

while command != "Christmas":
    if int(command) <= 16:
        kids += 1
        toys += 1
    elif int(command) > 16:
        adults += 1
        sweaters += 1

    command = input()

money_for_toys = kids * 5
money_for_sweaters = adults * 15

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {money_for_toys}')
print(f'Money for sweaters: {money_for_sweaters}')