katerachi = int(input())

g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0
obshto_katerachi = 0

for grupa in range(katerachi):
    broi_hora = int(input())
    obshto_katerachi += broi_hora
    if broi_hora <= 5:
        g1 += broi_hora
    elif 6 <= broi_hora <= 12:
        g2 += broi_hora
    elif 13 <= broi_hora <= 25:
        g3 += broi_hora
    elif 26 <= broi_hora <= 40:
        g4 += broi_hora
    else:
        g5 += broi_hora

procent_g1 = g1 / obshto_katerachi * 100
procent_g2 = g2 / obshto_katerachi * 100
procent_g3 = g3 / obshto_katerachi * 100
procent_g4 = g4 / obshto_katerachi * 100
procent_g5 = g5 / obshto_katerachi * 100

print(f'{procent_g1:.2f}%')
print(f'{procent_g2:.2f}%')
print(f'{procent_g3:.2f}%')
print(f'{procent_g4:.2f}%')
print(f'{procent_g5:.2f}%')