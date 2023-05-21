import sys

n = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for i in range(n):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

sum_numbers -= max_num
diff = abs(max_num - sum_numbers)

if max_num == sum_numbers:
    print("Yes")
    print(f'Sum = {max_num}')
else:
    print("No")
    print(f'Diff = {diff}')