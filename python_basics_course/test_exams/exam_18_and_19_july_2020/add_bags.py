luggage_price_over_20_kg = float(input())
luggage_weight = float(input())
trip_days = int(input())
number_of_luggages = int(input())

luggage_price = 0


if luggage_weight < 10:
    luggage_price = luggage_price_over_20_kg * 0.2
elif 10 <= luggage_weight <= 20:
    luggage_price = luggage_price_over_20_kg * 0.5
elif luggage_weight > 20:
    luggage_price = luggage_price_over_20_kg

if trip_days > 30:
    luggage_price = (0.1 * luggage_price) + luggage_price
elif 7 <= trip_days <= 30:
    luggage_price = (0.15 * luggage_price) + luggage_price
elif trip_days < 7:
    luggage_price = (0.4 * luggage_price) + luggage_price

print(f'The total price of bags is: {(number_of_luggages * luggage_price):.2f} lv.')