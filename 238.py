# LeetCode
# 238
# Product of Array Except Self
# Medium
# https://leetcode.com/problems/product-of-array-except-self/
# Array, Prefix Sum


# # My First Attempt
# def product(nums):
#     result = []

#     # for i in range(0, len(nums)):
#     #     p = 1

#     #     for j in range(0, len(nums)):            
#     #         if i != j:
#     #             p *= nums[j]
                
#     #     result.append(p)
#     for i in range(0, len(nums)):
#         print(nums[~i])

#     return result

# print(product([1,2,3,4]))
# print(product([-1,1,0,-3,3]))

from typing import List


# Time Complexity O(n), with no extra memory
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # from beginning to end
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
    

print(Solution().productExceptSelf(nums = [1,2,3,4]))
print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))
