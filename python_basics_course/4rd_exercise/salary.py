browser_tabs = int(input())
salary = float(input())


for i in range(browser_tabs):
    current_website = input()
    if current_website == 'Facebook':
        salary -= 150
    elif current_website == 'Instagram':
        salary -= 100
    elif current_website == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(f'{salary:.0f}')