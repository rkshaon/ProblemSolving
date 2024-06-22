# LeetCode
# 153. Find Minimum in Rotated Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[left] <= nums[mid] and nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[left]


a = Solution()
print(a.findMin(nums = [3,4,5,1,2]))
print(a.findMin(nums = [4,5,6,7,0,1,2]))
print(a.findMin(nums = [11,13,15,17]))