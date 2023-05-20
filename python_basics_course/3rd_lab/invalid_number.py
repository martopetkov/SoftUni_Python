chislo = int(input())

valid = 100 <= chislo <= 200 or chislo == 0
if not valid:
    print('invalid')