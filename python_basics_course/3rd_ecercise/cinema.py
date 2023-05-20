tip_projekciq = input()
redove = int(input())
koloni = int(input())
mesta_v_zalata = redove * koloni
pechalba = 0

if tip_projekciq == 'Premiere':
    pechalba = mesta_v_zalata * 12
elif tip_projekciq == 'Normal':
    pechalba = mesta_v_zalata * 7.50
elif tip_projekciq == 'Discount':
    pechalba = mesta_v_zalata * 5

print(f'{pechalba:.2f} leva')