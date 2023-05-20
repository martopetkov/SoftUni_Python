money = float(input())
godina = int(input())

ivan_year = 18
money_spent = 12000

for i in range(1800, godina):
    if i % 2 == 0:
        money -= money_spent
        ivan_year += 1
    else:
        money -= money_spent + 50 * ivan_year
        ivan_year += 1

n = abs(money - money_spent)

if money_spent >= money:
    print(f'Yes! He will live a carefree life and will have {n:.2f} dollars left.')
else:
    print(f'He will need {n:.2f} dollars to survive.')


