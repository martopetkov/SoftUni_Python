money_list = input().split(", ")
money_list_as_int = []
for el in money_list:
    money_list_as_int.append(int(el))

num_of_beggars = int(input())
final_sum = []
starting_index = 0

while starting_index < num_of_beggars:
    sum_for_current_beggar = 0

    for current_index in range(starting_index, len(money_list_as_int), num_of_beggars):
        sum_for_current_beggar += money_list_as_int[current_index]

    final_sum.append(sum_for_current_beggar)
    starting_index += 1

print(final_sum)