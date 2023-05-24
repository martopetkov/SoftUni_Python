capacity = float(input())
n = 1

while True:
    suitcase = input()
    if suitcase == "End":
        print(f"Congratulations! All suitcases are loaded!")
        break
    volume = float(suitcase)

    if n % 3 == 0:
        volume += (10 / 100) * volume
    if capacity < volume:
        print(f"No more space!")
        break
    else:
        n += 1
    capacity -= volume

print(f"Statistic: {n - 1} suitcases loaded.")