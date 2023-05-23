needed_sum = int(input())

new_sum_kesh = 0
new_sum_karta = 0
total_sum = 0  # needed_sum - (new_sum_karta + new_sum_kesh)
plashtane_s_karta = 0
plashtane_v_kesh = 0
counter = 0

while total_sum <= needed_sum:
    counter += 1
    command = input()
    if command == 'End':
        print('Failed to collect required money for charity.')
        break
    if counter % 2 == 0:
        if int(command) < 10:
            print('Error in transaction!')
        else:
            plashtane_s_karta += 1
            new_sum_karta += int(command)
            total_sum += int(command)
            print('Product sold!')
        if int(command) > 100:
            print('Error in transaction!')
        else:
            plashtane_v_kesh += 1
            new_sum_kesh += int(command)
            total_sum += int(command)
            print('Product sold!')
    if total_sum >= needed_sum:
        break

average_kesh = new_sum_kesh / plashtane_v_kesh
average_karta = new_sum_karta / plashtane_s_karta
if total_sum >= needed_sum:
    print(f'Average CS: {average_kesh:.2f}')
    print(f'Average CC: {average_karta:.2f}')