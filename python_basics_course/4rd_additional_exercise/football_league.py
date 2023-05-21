kapacitet_stadion = int(input())
total_fans = int(input())

sektor_a =0
sektor_b = 0
sektor_v = 0
sektor_g = 0


for i in range(total_fans):
    sektor = input()
    if sektor == "A":
        sektor_a += 1
    elif sektor == 'B':
        sektor_b += 1
    elif sektor == 'V':
        sektor_v += 1
    elif sektor == 'G':
        sektor_g += 1

procent_a = sektor_a / total_fans * 100
procent_b = sektor_b / total_fans * 100
procent_v = sektor_v / total_fans * 100
procent_g = sektor_g / total_fans * 100
total_procent = total_fans / kapacitet_stadion * 100

print(f'{procent_a:.2f}%')
print(f'{procent_b:.2f}%')
print(f'{procent_v:.2f}%')
print(f'{procent_g:.2f}%')
print(f'{total_procent:.2f}%')