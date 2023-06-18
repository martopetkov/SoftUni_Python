items = input().split("|")
line = input()

while line != "Yohoho!":
    command = line.split()

    if "Loot" in command:
        for i in range(1, len(command)):
            if command[i] not in items:
                items.insert(0, command[i])

    elif "Drop" in command:
        index = int(command[1])
        if 0 <= index < len(items):
            loot = items[index]
            items.pop(index)
            items.append(loot)

    elif "Steal" in command:
        count = int(command[1])
        if count <= len(items):
            last_loots = items[len(items) - count:len(items)]
            print(", ".join(last_loots))
            del items[len(items) - count:]
        elif count > len(items):
            last_loots = items[0::]
            print(", ".join(last_loots))
            del items[0::]

    line = input()

if len(items) > 0:
    average = 0
    for i in items:
        average += len(i)
    print(f"Average treasure gain: {(average / len(items)):.2f} pirate credits.")
else:
    print("Failed treasure hunt.")
