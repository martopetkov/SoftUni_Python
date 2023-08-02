line = input()
empty_list = []

while line != "end":
    command = line.split()

    if command[0] == "Chat":
        empty_list.append(command[1])

    elif command[0] == "Delete":
        if command[1] in empty_list:
            empty_list.remove(command[1])

    elif command[0] == "Edit":
        if command[1] in empty_list:
            index = empty_list.index(command[1])
            empty_list[index] = command[2]

    elif command[0] == "Pin":
        if command[1] in empty_list:
            empty_list.remove(command[1])
            empty_list.append(command[1])

    elif command[0] == "Spam":
        for message in command[1:]:
            empty_list.append(message)

    line = input()

[print(element) for element in empty_list]