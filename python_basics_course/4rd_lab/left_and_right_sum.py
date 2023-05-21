broi_chisla = int(input())

left_sum = 0
right_sum = 0

for num in range(1, broi_chisla + 1):
    left_sum += int(input())
for num in range(1, broi_chisla + 1):
    right_sum += int(input())

diff = abs(left_sum - right_sum)

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {diff}')