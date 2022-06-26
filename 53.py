# LeetCode
# 53. Maximum Subarray
# Easy
# https://leetcode.com/problems/maximum-subarray/

# def max_sub_array(nums):
#     max_sum = nums[0]
#     current_sum = nums[0]
#     for i in range(1, len(nums)):
#         current_sum = max(nums[i], current_sum + nums[i])
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# def max_sub_array(nums):
#     max_sum = 0
#     return max_sum

def max_sub_array(nums):
    max_sub = nums[0]
    current_sum = 0

    for n in nums:
        if current_sum < 0:
            current_sum = 0
        
        current_sum += n

        max_sub = max(max_sub, current_sum)

    return max_sub

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
print(max_sub_array([1]))
print(max_sub_array([5,4,-1,7,8]))
print(max_sub_array([-2,2,5,-11,6]))