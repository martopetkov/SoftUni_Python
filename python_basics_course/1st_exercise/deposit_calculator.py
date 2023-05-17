depozit = int(input())
srok = int(input())
glh = float(input()) / 100

lihva = depozit * glh
lihva_za_1_mesec = lihva / 12
total_sum = depozit + srok * lihva_za_1_mesec
print(total_sum)