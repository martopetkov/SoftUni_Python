items = input().split(", ")


while True:
    line = input()
    if line == "Craft!":
        print(*items, sep=", ")
        break

    command_args = line.split(" - ")
    command = command_args[0]

    if command == "Collect":
        item = command_args[1]
        if item not in items:
            items.append(item)

    elif command == "Drop":
        item = command_args[1]
        if item in items:
            items.remove(item)

    elif command == "Combine Items":
        second_split = command_args[1].split(":")
        old_item = second_split[0]
        new_item = second_split[1]

        if old_item in items:
            old_index = items.index(old_item)
            items.insert(old_index + 1, new_item)

    elif command == "Renew":
        item = command_args[1]
        if item in items:
            items.remove(item)
            items.append(item)

