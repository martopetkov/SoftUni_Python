first_letter = ord(input())
last_letter = ord(input())
middle_letter = input()

combination_counter = 0

for i in range(first_letter, last_letter + 1):
    for j in range(first_letter, last_letter + 1):
        for k in range(first_letter, last_letter + 1):

            if chr(i) != middle_letter and chr(j) != middle_letter and chr(k) != middle_letter:
                combination_counter += 1

                print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
print(combination_counter)