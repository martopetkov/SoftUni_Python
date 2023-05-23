n1 = int(input())
n2 = int(input())

for num in range(n1, n2 + 1):
    sum_even = 0
    sum_odd = 0
    num_to_str = str(num)

    for i in range(len(num_to_str)):
        if i % 2 == 0:
            sum_odd += int(num_to_str[i])
        else:
            sum_even += int(num_to_str[i])

    if sum_odd == sum_even:
        print(num, end=' ')

##### VTORI NACHIN! ######
n1 = int(input())
n2 = int(input())

for num in range(n1, n2 + 1):
    sum_even = 0
    sum_odd = 0
    num_to_str = str(num)

    for i, char in enumerate(num_to_str): #novo
        if i % 2 == 0:
            sum_odd += int(char) #novo
        else:
            sum_even += int(char) #novo

    if sum_odd == sum_even:
        print(num, end=' ')