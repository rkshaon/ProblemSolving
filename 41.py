# 41
# First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

# TLE Solution, answer is right But TLE
# def first_missing_positive(nums):
#     index = 1
#     nums = [x for x in nums if x > 0]
#     nums.sort()

#     for n in range(len(nums)):
#         if index in nums:
#             index += 1
#         else:
#             return index
        
#     return index

def first_missing_positive(nums):
    n = len(nums)

    # rearranging elements for correcting position
    for i in range(n):
        while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # finding the missing number if that is not in correct position
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # when every elements is in correct position then the answer is length + 1
    return n + 1

print(first_missing_positive(nums = [1,2,0]))
print(first_missing_positive(nums = [3,4,-1,1]))
print(first_missing_positive(nums = [7,8,9,11,12]))