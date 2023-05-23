shirina = int(input())
daljina = int(input())
visochina = int(input())

obem = shirina * daljina * visochina

while obem > 0:
    command = input()
    if command == 'Done':
        print(f'{obem} Cubic meters left.')  #printa moje da ne e tuk, a v else
        break
    obem -= int(command)

if obem <= 0:
    print(f'No more free space! You need {abs(obem)} Cubic meters more.')

# else:
# print(f'{obem} Cubic meters left.')