money_list = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for idx in range(len(money_list)):
    beggar_idx = idx % beggars_count
    num = int(money_list[idx])
    beggars[beggar_idx] += num

print(beggars)
