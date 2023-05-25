from math import ceil

num_of_days = int(input())
kilometers = float(input())

total_kms = 0
total_kms += kilometers

for d in range(1, num_of_days + 1):
    percent_increase = float(input())
    new_kms = kilometers + ((kilometers * percent_increase) / 100)
    total_kms += new_kms
    kilometers = new_kms


diff = abs(1000 - total_kms)

if total_kms >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers)")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")