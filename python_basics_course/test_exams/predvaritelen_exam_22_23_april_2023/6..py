k_num = input()
l_num = input()
m_num = input()
n_num = input()

counter = 0
end = False

for k1 in range(int(k_num[0]), 9):
    for l1 in range(9, int(l_num[0])-1, -1):
        for m1 in range(int(m_num[0]), 9):
            for n1 in range(9, int(n_num[0])-1, -1):
                i = int(str(k1)+str(l1))
                j = int(str(m1)+str(n1))
                if k1 % 2 == 0 and m1 % 2 == 0 and l1 % 2 != 0 and n1 % 2 != 0:
                    if i != j:
                        counter += 1
                        print(f"{k1}{l1} - {m1}{n1}")
                    else:
                        print("Cannot change the same player.")
                    if counter == 6:
                        end = True
                if end:
                    break
            if end:
                break
        if end:
            break
    if end:
        break



