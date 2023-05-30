string = [int(x) for x in input().split(", ")]

for i in string:
    if i == 0:
        string.remove(i)
        string.append(i)
print(string)



#2
string = [int(x) for x in input().split(", ")]

for i in string:
    if i == 0:
        string.append(string.pop(string.index(i)))
print(string)



#3
string = [int(x) for x in input().split(", ")]

for i in string:
    if i == 0:
        first = string.index(i)
        second = string.pop(first)
        string.append(second)
print(string)
