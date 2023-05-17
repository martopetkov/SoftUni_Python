gradusi = float(input())

if 26.00 <= gradusi <= 35:
        print("Hot")
elif 20.1 <= gradusi <= 25.9:
        print("Warm")
elif 15.00 <= gradusi <= 20.00:
        print("Mild")
elif 12.00 <= gradusi <= 14.9:
        print("Cool")
elif 5.00 <= gradusi <= 11.9:
        print("Cold")
else:
        print("unknown")
