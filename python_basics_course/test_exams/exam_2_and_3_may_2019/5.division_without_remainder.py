numbers = int(input())

p1 = 0
p2 = 0
p3 = 0

for n in range(1, numbers +1):
    k = int(input())
    if k % 2 == 0:
        p1 += 1
    if k % 3 == 0:
        p2 += 1
    if k % 4 == 0:
        p3 += 1

p1_procent = (p1 * 100) / numbers
p2_procent = (p2 * 100) / numbers
p3_procent = (p3 * 100) / numbers

print(f"{p1_procent:.2f}%")
print(f"{p2_procent:.2f}%")
print(f"{p3_procent:.2f}%")

