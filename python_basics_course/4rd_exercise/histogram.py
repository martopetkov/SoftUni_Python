n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(n):
    curr_number = int(input())
    if curr_number < 200:
        p1_count += 1
    elif curr_number <= 399:
        p2_count += 1
    elif curr_number <= 599:
        p3_count += 1
    elif curr_number <= 799:
        p4_count += 1
    elif 800 <= curr_number:
        p5_count += 1

p1_procent = p1_count / n * 100
p2_procent = p2_count / n * 100
p3_procent = p3_count / n * 100
p4_procent = p4_count / n * 100
p5_procent = p5_count / n * 100

print(f'{p1_procent:.2f}%')
print(f'{p2_procent:.2f}%')
print(f'{p3_procent:.2f}%')
print(f'{p4_procent:.2f}%')
print(f'{p5_procent:.2f}%')
