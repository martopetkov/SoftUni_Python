veggie_price = float(input())
frutty_price = float(input())
total_kilos_vegie = int(input())
total_kilos_frutty = int(input())

profit = ((veggie_price * total_kilos_vegie) + (frutty_price * total_kilos_frutty)) / 1.94
print(f'{profit:.2f}')