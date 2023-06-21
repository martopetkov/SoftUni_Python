def is_index_in_range(idx, seq):
    if 0 <= idx < len(seq):
        return True
    return False


pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())


is_running = True
while is_running:
    line = input()
    if line == "Retire":
        break

    command_args = line.split()
    command = command_args[0]

    if command == "Fire":
        idx = int(command_args[1])
        damage = int(command_args[2])
        if not is_index_in_range(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            is_running = False
            print("You won! The enemy ship has sunken.")

    elif command == "Defend":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        damage = int(command_args[3])
        if not is_index_in_range(start_idx, pirate_ship) or not is_index_in_range(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[start_idx] <= 0:
                is_running = False
                print("You lost! The pirate ship has sunken.")
                break

    elif command == "Repair":
        idx = int(command_args[1])
        health = int(command_args[2])
        if not is_index_in_range(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_health, pirate_ship[idx] + health)

    elif command == "Status":
        counter = 0
        for idx in pirate_ship:
            if idx < 0.2 * max_health:
                counter += 1
        print(f"{counter} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")