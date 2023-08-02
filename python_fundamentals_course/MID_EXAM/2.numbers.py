sequence = [int(x) for x in input().split()]

while True:
    line = input()
    if line == "Finish":
        print(" ".join(str(x) for x in sequence))
        break

    command = line.split()
    if command[0] == "Add":
        value = int(command[1])
        sequence.append(value)

    elif command[0] == "Remove":
        value = int(command[1])
        if value in sequence:
            sequence.remove(value)

    elif command[0] == "Replace":
        value = int(command[1])
        if value in sequence:
            index = sequence.index(value)
            sequence[index] = int(command[2])

    elif command[0] == "Collapse":
        value = int(command[1])
        sequence = [i for i in sequence if i >= value]

