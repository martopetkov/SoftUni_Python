def multiplication(nums):
    multip = 1
    for n in nums:
        multip *= n
    return multip


n1 = int(input())
n2 = int(input())
n3 = int(input())
numbers = [n1, n2, n3]
result = multiplication(numbers)
if result > 0:
    print("positive")
elif result < 0:
    print("negative")
else:
    print("zero")