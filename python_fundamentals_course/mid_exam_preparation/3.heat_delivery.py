neighborhood = [int(x) for x in input().split("@")]
line = input()


neighborhood_len = len(neighborhood)
index = 0


while line != "Love!":
    index += int(line.split()[-1])

    if index >= neighborhood_len:
        index = 0

    if neighborhood[index] > 2:
        neighborhood[index] -= 2
    else:
        if neighborhood[index] != 0:
            neighborhood[index] -= 2
            text = "has"
        else:
            text = "already had"
        print(f"Place {index} {text} Valentine's day.")

    line = input()

print(f"Cupid's last position was {index}.")

failed_houses = sum(1 for x in neighborhood if x != 0)
if failed_houses:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")