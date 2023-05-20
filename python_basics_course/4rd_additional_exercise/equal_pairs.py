pairs = int(input())

previous_sum = 0
previous_diff = 0
max_diff = 0
is_equal = True

for i in range(1, pairs + 1):
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2
    if i == 1:
        previous_sum = sum
    elif previous_sum == sum:
        is_equal = True
    else:
        is_equal = False
        if sum > previous_sum:
            previous_diff = sum - previous_sum
        else:
            previous_diff = previous_sum - sum
        if previous_diff > max_diff:
            max_diff = previous_diff
        previous_sum = sum
if is_equal:
    print(f"Yes, value={previous_sum}")
else:
    print(f'No, maxdiff={max_diff}')

