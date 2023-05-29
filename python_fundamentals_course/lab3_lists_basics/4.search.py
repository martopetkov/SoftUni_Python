lines = int(input())
word = input()
strings = []
filtered_strings = []

for _ in range(lines):
    text = input()
    strings.append(text)

    if word in text:
        filtered_strings.append(text)

print(strings)
print(filtered_strings)

