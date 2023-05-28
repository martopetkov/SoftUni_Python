capacity = 255
volume = 0
lines = int(input())

for liters in range(lines):
    water = int(input())
    if volume + water > capacity:
        print("Insufficient capacity!")
    else:
        volume += water

print(volume)

