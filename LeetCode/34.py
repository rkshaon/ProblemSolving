# LeetCode
# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# O(log n) solution
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums=nums, target=target, leftBias=True)
        right = self.binSearch(nums=nums, target=target, leftBias=False)

        return [left, right]

    # leftBiased = [True/False], if false, result is rightBiased
    def binSearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        index = -1

        while left <= right:
            mid = (left + right) // 2

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                index = mid

                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return index


a = Solution()

print(a.searchRange(nums = [5,7,7,8,8,10], target = 8))
print(a.searchRange(nums = [5,7,7,8,8,10], target = 7))
print(a.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(a.searchRange(nums = [], target = 0))

# Explain 1
# nums = [5,7,7,8,8,10], target = 8
# leftBias = True
# left = 0, right = 5
# mid = (0+5) // 2 = 2
# 8 > 7, so left = 2 + 1 = 3
# mid = (3+5) // 2 = 4
# 8 == 8, so index = 4
# leftBias is True, so right = 4 - 1 = 3, left = 3
# mid = 3
# 8 ==8, so index = 3
# left and right is equal, so loop break
# return 3
# nums = [5,7,7,8,8,10], target = 8
# leftBias = False
# left = 0, right = 5
# mid = (0+5) // 2 = 2
# 8 > 7, so left = 2 + 1 = 3
# mid = 4
# 8 == 8, so index = 4
# leftBias is False, so, left = 3 + 1, right = 5
# mid = (4+5) // 2 = 4
# 8 == 8, so index = 4
# leftBias is False, so left = 4 + 1 = 5, right = 5
# 8 < 10, so left = 5 + 1
# left is equal or greater than right, so break
# return 4