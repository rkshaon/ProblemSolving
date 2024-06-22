# 26
# Remove Duplicates from Sorted Array
# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Array, Two Pointer


from typing import List


# Solution: Two Pointer
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
            
        return left, nums




print(Solution().removeDuplicates(nums = [1,1,2]))
print(Solution().removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))