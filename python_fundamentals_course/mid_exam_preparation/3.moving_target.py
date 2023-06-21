targets = [int(x) for x in input().split()]

line = input()

while line != "End":
    command, index, value = [int(x) if x[-1].isdigit() else x for x in line.split()]
    # идеята на горния ред е да проверим дали само последния елемент е число (заради Енд-а)
    valid_index = True
    if not 0 <= index < len(targets):
        valid_index = False

    elif command == "Shoot":
        targets[index] -= value
        if targets[index] <= 0:
            del targets[index]

    if command == "Add":
        if valid_index:
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        start_index = index - value
        end_index = index + value + 1
        if 0 <= start_index < end_index < len(targets):
            del targets[start_index:end_index]
        else:
            print("Strike missed!")

    line = input()


print(*targets, sep="|")