n = int(input())
current = 1
is_current_bigger_than_n = False
# is_finished = False


for row in range(1, n + 1):
    for num in range(1, row + 1):
        if current > n:
            is_current_bigger_than_n = True
            break
        print(current, end=' ')
        current += 1
    if is_current_bigger_than_n:
        break
    print()