# 35. Search Insert Position
# Easy
# Array, Binary Search
# https://leetcode.com/problems/search-insert-position/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums = set(nums)
        nums.add(target)
        nums = list(nums)

        return nums.index(target)


a = Solution()
print(a.searchInsert(nums = [1,3,5,6], target = 5))
print(a.searchInsert(nums = [1,3,5,6], target = 2))
print(a.searchInsert(nums = [1,3,5,6], target = 7))