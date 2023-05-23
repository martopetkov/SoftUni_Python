is_prime = True
sum_prime_nums = 0
sum_non_prime_nums = 0


command = input()
while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print('Number is negative.')
    else:
        for i in range(2, current_num):
            if current_num % i == 0:
                is_prime = False
                break

        if is_prime:
            sum_prime_nums += current_num
        else:
            sum_non_prime_nums += current_num
            is_prime = True
    command = input()

print(f'Sum of all prime numbers is: {sum_prime_nums}')
print(f'Sum of all non prime numbers is: {sum_non_prime_nums}')