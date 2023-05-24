strawberry_price = float(input())
banana_kilos = float(input())
orange_kilos = float(input())
malini_kilos = float(input())
strawberry_kilos = float(input())

malini_price = strawberry_price / 2
orange_price = malini_price * 0.6
banana_price = malini_price * 0.2

total_sum = (strawberry_price * strawberry_kilos) + (banana_price * banana_kilos) + (orange_price * orange_kilos) + (malini_price * malini_kilos)
print(f'{total_sum:.2f}')
