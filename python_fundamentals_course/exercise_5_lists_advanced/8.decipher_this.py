line = input().split()

new_word = []
for word in line:
    num = ''
    for el in word:
        if el.isdigit():
            num = num + el
            new_word.append(num)


        symbol = chr(int(num))

    print(word)
    print(new_word)



