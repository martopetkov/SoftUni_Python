square_meters_for_greenings = float(input())
price_without_discount = square_meters_for_greenings * 7.61
discount = price_without_discount * 0.18
final_price = price_without_discount - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is {discount} lv.")