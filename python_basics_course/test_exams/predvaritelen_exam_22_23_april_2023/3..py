num_people = int(input())
season = input()

price = 0

if num_people <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.50
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86

elif num_people > 5:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        price = 85

trip_price = price * num_people

if season == "summer":
    trip_price *= 0.85
if season == "winter":
    trip_price *= 1.08

print(f'{trip_price:.2f} leva.')