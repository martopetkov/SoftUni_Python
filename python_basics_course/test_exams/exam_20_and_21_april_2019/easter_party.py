guest_num = int(input())
price_covert = float(input())
budjet = float(input())

if 10 <= guest_num <= 15:
    price_covert *= 0.85
elif 15 < guest_num <= 20:
    price_covert *= 0.8
elif guest_num > 20:
    price_covert *= 0.75

cake_price = budjet * 0.1
total_sum = (guest_num * price_covert) + cake_price

diff = abs(total_sum - budjet)

if budjet >= total_sum:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')