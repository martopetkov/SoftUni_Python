def characters(a, b):
    result = []
    for i in range(ord(char1) + 1, ord(char2)):
        result.append(chr(i))
    return result


char1 = input()
char2 = input()

final_result = characters(char1, char2)
#print(final_result) - изкарва ги като лист
#print(' '.join(final_result))
print(*final_result)
#print(*final_result, sep = ' ')  - така също може да разопаковаме, но по дефаулт си е 1 празен спейс