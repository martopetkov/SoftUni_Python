wagons = int(input())
train = [0] * wagons
#train = [0 for num in range(wagons)]
command = input()

while command != "End":
    action = command.split()[0]
    if action == "add":
        n_people = int(command.split()[1])
        train[-1] += n_people
    elif action == "insert":
        idx = int(command.split()[1])
        n_people = int(command.split()[2])
        train[idx] += n_people
    elif action == "leave":
        idx = int(command.split()[1])
        n_people = int(command.split()[2])
        train[idx] -= n_people

    command = input()

print(train)
