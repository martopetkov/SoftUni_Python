list = input().split()
result = [el for el in list if len(el) % 2 == 0]
#wtori nachin za chetene na inputa:
#  result = list(filter(lambda x: len(x) % 2 == 0, input().split())))
print('\n'.join(result))

#wtori print:
#for el in result:
    #print(result)