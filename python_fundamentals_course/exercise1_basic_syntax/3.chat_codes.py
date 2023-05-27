n = int(input())

for i in range(n):
    k = int(input())
    if k == 88:
        print("Hello")
    elif k == 86:
        print("How are you?")
    elif k != 88 and k != 86 and k < 88:
        print("GREAT!")
    else:
        print('Bye.')