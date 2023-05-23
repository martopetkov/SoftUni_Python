nums = [1, 3, 6, 5, 6]

for index in range(len(nums) -1, -1, -1):
    if nums[index] == 5:
        print(index)
