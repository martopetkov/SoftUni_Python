flower_price_per_kg = float(input())
kg_flower = float(input())
kg_sugar = float(input())
eggs_box = int(input())
packets_maya = int(input())

sugar_price = flower_price_per_kg * 0.75
egg_box_price = flower_price_per_kg * 1.1
maya_price = sugar_price * 0.2

total_sum = (flower_price_per_kg * kg_flower) + (sugar_price * kg_sugar) + (egg_box_price * eggs_box) + (maya_price * packets_maya)

print(f'{total_sum:.2f}')