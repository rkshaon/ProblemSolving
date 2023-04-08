# 35. Search Insert Position
# Easy
# Array, Binary Search
# https://leetcode.com/problems/search-insert-position/

from typing import List

import bisect

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)


a = Solution()
print(a.searchInsert(nums = [1,3,5,6], target = 5))
print(a.searchInsert(nums = [1,3,5,6], target = 2))
print(a.searchInsert(nums = [1,3,5,6], target = 7))