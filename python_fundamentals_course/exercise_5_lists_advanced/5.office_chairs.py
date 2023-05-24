rooms = int(input())

free_chairs = 0
needs_chairs = True
for room in range (1, rooms +  1):
    line = input().split()
    chairs, visitors = len(line[0]), int(line[1])

    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        needs_chairs = False

    else:
        free_chairs += chairs - visitors

if needs_chairs:
    print(f"Game On, {free_chairs} free chairs left")