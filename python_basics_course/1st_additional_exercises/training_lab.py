daljina = float(input()) * 100
shirina = float(input()) * 100

seat_daljina = 120
seat_shirina = 70

number_of_seat_daljina = (daljina - 100) // seat_daljina
number_of_lines = shirina // seat_shirina

number_of_all_seats = number_of_seat_daljina * number_of_lines - 3
print(number_of_all_seats)