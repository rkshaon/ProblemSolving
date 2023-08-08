# LeetCode
# 154. Find Minimum in Rotated Sorted Array II
# Array, Binary Search
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List



class Solution:
    # def findMin(self, nums: List[int]) -> int:
    #     return self.search(nums=nums, left=0, right=len(nums)-1)


    # def search(self, nums: List[int], left: int, right: int) -> int:
    #     if left == right:
    #         return nums[left]
        
    #     mid = (left + right) // 2

    #     if nums[mid] > nums[right]:
    #         return self.search(nums=nums, left=mid+1, right=right)

    #     elif nums[mid] < nums[right]:
    #         return self.search(nums=nums, left=left, right=mid)
        
    #     else:
    #         left_min = self.search(nums=nums, left=left, right=mid)
    #         right_min = self.search(nums=nums, left=mid+1, right=right)
            
    #         return min(left_min, right_min)
    def findMind(self, nums: List[int]) -> int:
        pass


a = Solution()

print(a.findMin(nums = [1,3,5]))
print(a.findMin(nums = [2,2,2,0,1]))
print(a.findMin(nums = [1,1]))