cells = input().split("#")
water = int(input())
total_fire = 0
processed_cells = []

for cell in cells:
    cells_args = cell.split(" = ")
    level = cells_args[0]
    value = int(cells_args[1])

    if level == 'High' and (value < 81 or value > 125):
        continue
    if level == 'Medium' and (value < 51 or value > 80):
        continue
    if level == 'Low' and (value < 1 or value > 50):
        continue

    if value > water:
        continue

    water -= value
    total_fire += value
    processed_cells.append(value)

effort = total_fire * 0.25
print("Cells:")
for cell in processed_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")