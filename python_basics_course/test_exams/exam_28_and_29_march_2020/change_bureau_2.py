sum_bitcoins = int(input())
sum_chineese_uans = float(input())
commision = float(input())

sum_leva_to_euro = ((sum_bitcoins * 1168) + ((sum_chineese_uans * 0.15) * 1.76)) / 1.95
sum_commission = (commision * sum_leva_to_euro) / 100

print(f'{(sum_leva_to_euro - sum_commission):.2f}')