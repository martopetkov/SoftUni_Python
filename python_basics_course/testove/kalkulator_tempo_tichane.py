name = input("Въдете име: " )
distance = float(input("Въведете разстояние в км: "))
minutes = float(input("Въведете времетраене в мин: "))
tempo = ''

pace = distance / minutes

if pace < 10:
    tempo = "бавно"
elif pace == 10:
    tempo = "средно"
else:
    tempo = "бързо"

print(f'{name} е изтичал/а {distance:.2f} км. за {minutes:.2f} минути с/със {tempo} темпо и скорост от {pace:.2f}км/ч. Добра работа!')

