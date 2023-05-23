first_num_max_range = int(input())
second_num_max_range = int(input())
third_num_max_range = int(input())

for x in range(1, first_num_max_range + 1):
    if x % 2 == 0:
        counter = 0

        for y in range(2, second_num_max_range + 1):
            if y != 4 and y != 6 and y != 8 and y != 9:

                for z in range (1, third_num_max_range + 1):
                    if z % 2 == 0:
                        print(f'{x} {y} {z}', end=' ')
                        print()


