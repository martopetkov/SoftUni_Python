num_kozunaci = float(input())
num_eggs = float(input())
kilos_coockies = float(input())


sum = (num_kozunaci * 3.20) + (num_eggs * 4.35 ) + (kilos_coockies * 5.4)
eggs_paint = num_eggs * 12 * 0.15

total_sum = sum + eggs_paint

print(f'{total_sum:.2f}')