nums = list(map(int, input().split(", ")))
print([index for index in range (len(nums)) if nums[index] % 2 == 0])

#втори начин - принта само е различен
nums = list(map(int, input().split(", ")))
print(list(map(lambda x: nums.index(x), list(filter(lambda x: x % 2 == 0, nums)))))
