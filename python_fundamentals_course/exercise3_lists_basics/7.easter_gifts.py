gifts = input().split()
line = input()

while line != "No Money":
    command_args = line.split()
    command = command_args[0]
    gift = command_args[1]

    if command == "OutOfStock":
        for idx in range(len(gifts)):
            if gifts[idx] == gift:
                gifts[idx] = "None"
    if command == "Required":
        idx = int(command_args[2])
        if 0 <= idx < len(gifts):
            gifts[idx] = gift
    if command == "JustInCase":
        gifts[-1] = gift
    line = input()

for gift in gifts:
    if gift == "None":
        continue
    print(gift, end=' ')
