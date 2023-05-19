junior_bikers = int(input())
senior_bikers = int(input())
track_type = input()
tax = 0
costs = 0

if track_type == 'trail':
    tax = (junior_bikers * 5.5) + (senior_bikers * 7)
elif track_type == 'cross-country':
    tax = (junior_bikers * 8) + (senior_bikers * 9.5)
    if (junior_bikers + senior_bikers) >= 50:
        tax = ((junior_bikers * 8) + (senior_bikers * 9.5)) * 0.75
elif track_type == 'downhill':
    tax = (junior_bikers * 12.25) + (senior_bikers * 13.75)
elif track_type == 'road':
    tax = (junior_bikers * 20) + (senior_bikers * 21.5)

costs = tax * 0.05
diff = tax - costs

print(f'{diff:.2f}')