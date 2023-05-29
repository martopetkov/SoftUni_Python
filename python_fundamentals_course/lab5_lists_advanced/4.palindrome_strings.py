words = input().split(" ")
palindrome = input()
palindromes = []

for el in words:
    if el == "".join(reversed(el)):
        palindromes.append(el)
#•	We use the join() method with the reversed() method because reversed()
# returns an iterator, not a string, so we should make it into one.
print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")

#____________________________________________________________________________
#мой начин
words = input().split(" ")
palindrome = input()
palindromes = []
counter = 0

for el in words:
    if el == el[::-1]:
        palindromes.append(el)

for el in palindromes:
    if el == palindrome:
        counter += 1

print(palindromes)
print(f"Found palindrome {counter} times")

