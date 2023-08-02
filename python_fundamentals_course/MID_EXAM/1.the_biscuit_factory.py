from math import floor

num_of_biscuits = int(input())
num_of_workers = int(input())
other_factory = int(input())

usual_production = floor(num_of_biscuits * num_of_workers)
lowered_production = floor(usual_production * 0.75)
my_factory_prod = 0

for day in range(1, 31):
    if day % 3 == 0:
        my_factory_prod += lowered_production
    else:
        my_factory_prod += usual_production

print(f"You have produced {my_factory_prod} biscuits for the past month.")
difference = abs(my_factory_prod - other_factory)

if my_factory_prod > other_factory:
    print(f"You produce {(difference / other_factory * 100):.2f} percent more biscuits.")

else:
    print(f"You produce {(difference / other_factory * 100):.2f} percent less biscuits.")