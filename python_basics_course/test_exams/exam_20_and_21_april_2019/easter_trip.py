destination = input()
dates = input()
nights = int(input())

price = 0

if destination == "France":
    if dates == '21-23':
        price = 30 * nights
    elif dates == '24-27':
        price = 35 * nights
    elif dates == '28-31':
        price = 40 * nights

if destination == "Italy":
    if dates == '21-23':
        price = 28 * nights
    elif dates == '24-27':
        price = 32 * nights
    elif dates == '28-31':
        price = 39 * nights
    
if destination == "Germany":
    if dates == '21-23':
        price = 32 * nights
    elif dates == '24-27':
        price = 37 * nights
    elif dates == '28-31':
        price = 43 * nights
        
print(f'Easter trip to {destination} : {price:.2f} leva.')