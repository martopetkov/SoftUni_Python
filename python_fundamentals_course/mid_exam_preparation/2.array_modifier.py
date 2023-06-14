elements = [int(x) for x in input().split()]

line = input()

while line != "end":

    if "decrease" in line:
        # for i in range(len(elements))
        #     elements[i] -= 1
        elements =[x - 1 for x in elements] # върти цикъл за да извади -1 от всички стойности
        line = input()
        continue

    command, index1, index2 = [x if x.isalpha() else int(x) for x in line.split()]

    if command == "swap":
        elements[index1], elements[index2] = elements[index2], elements[index1]

    if command == "multiply":
        elements[index1] *= elements[index2]

    line = input()

print(*elements, sep=", ")
