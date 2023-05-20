dni_prestoi = int(input())
nights = dni_prestoi - 1
place = input()
feedback = input()
price = 0
discount = 0

if place == 'room for one person':
    price = nights * 18

elif place == 'apartment':
    price = nights * 25
    if nights < 10:
        price *= 0.70
    elif 10 < nights < 15:
        price *= 0.65
    elif 15 < nights:
        price *= 0.5

elif place == 'president apartment':
    price = nights * 35
    if nights < 10:
        price *= 0.90
    elif 10 > nights < 15:
        price *= 0.85
    elif 15 <= nights:
        price *= 0.8

if feedback == 'positive':
    price *= 1.25
elif feedback == 'negative':
    price *= 0.9

print(f'{price:.2f}')