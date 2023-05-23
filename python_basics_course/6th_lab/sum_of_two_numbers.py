starting_interval = int(input())
ending_interval = int(input())
magic_number = int(input())

combination_count = 0
magic_number_condition = False
print_data = ''

for x in range(starting_interval, ending_interval + 1):
    for y in range(starting_interval, ending_interval + 1):
        combination_count += 1

        if x + y == magic_number:
            magic_number_condition = True
            print_data = f'Combination N:{combination_count} ({x} + {y} = {magic_number})'
            break

    if magic_number_condition:
        break

if magic_number_condition:
    print(print_data)
else:
    print(f'{combination_count} combinations - neither equals {magic_number}')