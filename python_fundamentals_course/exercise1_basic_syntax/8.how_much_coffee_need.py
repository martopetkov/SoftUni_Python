coffee_cup = 0

while True:
    command = input()
    if command == "END":
        break
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        coffee_cup += 1
    elif command == "CODING" or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        coffee_cup += 2
    else:
        continue

if coffee_cup > 5:
    print('You need extra sleep')
else:
    print(f"{coffee_cup}")