needed_sum = int(input())

new_sum_kesh = 0
new_sum_karta = 0
total_sum = 0
plashtane_s_karta = 0
plashtane_v_kesh = 0
counter = 0

while True:
    command = input()
    if command == 'End':
        print('Failed to collect required money for charity.')
        break
    counter += 1
    if counter % 2 == 0:
        if int(command) < 10:
            print('Error in transaction!')
        else:
            plashtane_s_karta += 1
            new_sum_karta += int(command)
            total_sum += int(command)
            print('Product sold!')
    else:
        if int(command) > 100:
            print('Error in transaction!')
        else:
            plashtane_v_kesh += 1
            new_sum_kesh += int(command)
            total_sum += int(command)
            print('Product sold!')
    if total_sum >= needed_sum:
        break

if total_sum >= needed_sum:
    average_kesh = new_sum_kesh / plashtane_v_kesh
    average_karta = new_sum_karta / plashtane_s_karta
    print(f'Average CS: {average_kesh:.2f}')
    print(f'Average CC: {average_karta:.2f}')