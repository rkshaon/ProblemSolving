# LeetCode
# 81. Search in Rotated Sorted Array II
# Medium
# Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Simple solution 1
        # if target in nums:
        #     return True
            
        # return False
        # More simple solution 2
        # return True if target in nums else False

        # Algorithmic solution
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == target or nums[right] == target:
                return True
            
            elif target > nums[left]:
                while left < right and nums[left+1] == nums[left]:
                    left += 1

                left += 1

            elif target < nums[right]:
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                    
                right -= 1
            
            else:
                break

        return False
    

a = Solution()

print(a.search(nums = [2,5,6,0,0,1,2], target = 0))
print(a.search(nums = [2,5,6,0,0,1,2], target = 3))