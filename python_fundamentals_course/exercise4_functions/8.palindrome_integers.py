def palidrome(nums):
    for i in nums:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


numbers = input().split(", ")
palidrome(numbers)

#втори начин:
def palidrome(nums):
    for i in nums:
        print(i == i[::-1])


numbers = input().split(", ")
palidrome(numbers)