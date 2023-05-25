from math import floor

turniri = int(input())
start_points = int(input())


w = 0
f = 0
sf = 0
final_points = 0

for poziciq in range (turniri):
    etap = input()
    if etap == "W":
        final_points += 2000
        w += 1
    elif etap == "F":
        final_points += 1200
        f += 1
    elif etap == "SF":
        final_points += 720
        sf += 1

average_points = final_points / (w + f + sf)
procent_specheleni_turniri = (w / turniri) * 100

print(f'Final points: {start_points + final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{procent_specheleni_turniri:.2f}%')
