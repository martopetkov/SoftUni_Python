command = input()

while command != "End":
    if command == "SoftUni":
        continue

    converted_line = ''
    for ch in command:
        converted_line += 2 * ch
    print(converted_line)

    command = input()

# lektora go reshava s while true - na ostavashto vreme 1 chas 03 minuti moje
# da se vidi reshenieto mu.

#koda ne raboti za key sensitive softuni/ SoftUni
