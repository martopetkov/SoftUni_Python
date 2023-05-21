days = int(input())
medics = 7
untreated = 0
treated = 0

for day in range(1, days + 1):
    if day % 3 == 0 and untreated > treated:
        medics += 1
    new_patients = int(input())
    diff = medics - new_patients
    if medics < new_patients:
        treated += medics
        untreated += abs(diff)
    else:
        treated += new_patients
print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')