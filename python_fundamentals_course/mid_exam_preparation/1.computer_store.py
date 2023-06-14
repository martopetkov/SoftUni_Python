
is_special = False
total_price = 0

while True:
    command = input()
    if command == "regular":
        break
    if command == "special":
        is_special = True
        break
    command = float(command)
    if command > 0:
        total_price += command
    else:
        print("Invalid price!")


taxes = total_price * 0.2
total_price_with_taxes = total_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    if is_special:
        print(f"Total price: {(total_price_with_taxes * 0.9):.2f}$")
    else:
        print(f"Total price: {total_price_with_taxes:.2f}$")