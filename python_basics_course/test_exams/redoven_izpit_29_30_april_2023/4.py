n = int(input())
m = int(input())
s = int(input())


for gifts in range(n, m + 1):
    if gifts % 2 == 0 and gifts % 3 == 0:
        if gifts == s:
            break
        print(f'{gifts}', end=' ')