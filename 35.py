# 35. Search Insert Position
# Easy
# Array, Binary Search
# https://leetcode.com/problems/search-insert-position/

from typing import List

import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # single line solution
        # return bisect.bisect_left(nums, target)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left


a = Solution()
print(a.searchInsert(nums = [1,3,5,6], target = 5))
print(a.searchInsert(nums = [1,3,5,6], target = 2))
print(a.searchInsert(nums = [1,3,5,6], target = 7))