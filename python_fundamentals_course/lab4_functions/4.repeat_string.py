text = input()
n = int(input())

repeat_as_lambda = lambda word, times: word * times
print(repeat_as_lambda(text, n))
