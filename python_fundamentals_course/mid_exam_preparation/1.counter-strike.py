energy = int(input())

won_battle = 0
is_won = True
while True:
    command = input()
    if command == "End of battle":
        break

    distance = int(command)
    if energy >= distance and energy > 0:
        energy -= distance
        won_battle += 1
    else:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {energy} energy")
        is_won = False
        break

    if won_battle % 3 == 0:
        energy += won_battle

if is_won:
    print(f"Won battles: {won_battle}. Energy left: {energy}")