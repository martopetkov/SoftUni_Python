first_num = input()
last_num = input()

for n1 in range(int(first_num[0]), int(last_num[0]) + 1):
    for n2 in range(int(first_num[1]), int(last_num[1]) + 1):
        for n3 in range(int(first_num[2]), int(last_num[2]) + 1):
            for n4 in range(int(first_num[3]), int(last_num[3]) + 1):
                if n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0 and n4 % 2 != 0:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')