budjet = float(input())
number_of_gpu = int(input())
number_of_cpu = int(input())
number_of_ram = int(input())

money_for_gpu = number_of_gpu * 250
money_for_cpu = (money_for_gpu * 0.35) * number_of_cpu
money_for_ram = (money_for_gpu * 0.10) * number_of_ram

total_sum = money_for_gpu + money_for_cpu + money_for_ram

if number_of_gpu > number_of_cpu:
    total_sum *= 0.85

diff = abs(budjet - total_sum)

if budjet >= total_sum:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')