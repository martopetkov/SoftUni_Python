wagons = int(input())
train = [0] * wagons
#train = [0 for num in range(wagons)]
command = input()

while command != "End":
    #в следващия ред правиме веднъж сплит и после заменяме само индекса му
    split_data = command.split()
    action = split_data[0]
    if action == "add":
        n_people = int(split_data[1])
        train[-1] += n_people
    elif action == "insert":
        idx = int(split_data[1])
        n_people = int(split_data[2])
        train[idx] += n_people
    elif action == "leave":
        idx = int(split_data[1])
        n_people = int(split_data[2])
        train[idx] -= n_people

    command = input()

print(train)
