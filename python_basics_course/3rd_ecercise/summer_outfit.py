gradusi = int(input())
day_time = input()
outfit = ''
shoes = ''


if day_time == 'Morning':
    if 10 <= gradusi <= 18:
        outfit = "Sweatshirt" ; shoes = "Sneakers"
    elif 18 < gradusi <= 24:
        outfit = "Shirt" ;  shoes = "Moccasins"
    elif gradusi >= 25:
        outfit = "T-Shirt" ; shoes = "Sandals"

elif day_time == 'Afternoon':
    if 10 <= gradusi <= 18:
        outfit = "Shirt" ; shoes = "Moccasins"
    elif 18 < gradusi <= 24:
        outfit = "T-Shirt" ; shoes = "Sandals"
    elif gradusi >= 25:
        outfit = "Swim Suit" ; shoes = "Barefoot"

elif day_time == 'Evening':
    if 10 <= gradusi <= 18:
        outfit = "Shirt" ; shoes = "Moccasins"
    elif 18 < gradusi <= 24:
        outfit = "Shirt" ; shoes = "Moccasins"
    elif gradusi >= 25:
        outfit = "Shirt" ; shoes = "Moccasins"

print(f"It's {gradusi} degrees, get your {outfit} and {shoes}.")