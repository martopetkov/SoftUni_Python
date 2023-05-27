while True:
    command = input()
    if command == "End":
        break

    if command == "SoftUni":
        continue
    for ch in command:
        print(f"{ch}{ch}", end='')
    print()

#raboti