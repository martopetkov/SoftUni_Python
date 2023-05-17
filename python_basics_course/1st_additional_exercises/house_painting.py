x = float(input())
y = float(input())
h = float(input())

#steni
stranichna_stena = ((x * y) - (1.5 * 1.5)) * 2 + ((x * x) - (1.2 * 2)) + (x * x)
green_paint = stranichna_stena / 3.4

#pokriv
pravoagalnik = 2 * (x * y) + (2 * (x * h / 2))
red_paint = pravoagalnik / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')