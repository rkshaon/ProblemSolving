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

        # Algorithmic solution 3
        # left, right = 0, len(nums) - 1

        # while left <= right:
        #     if nums[left] == target or nums[right] == target:
        #         return True
            
        #     elif target > nums[left]:
        #         while left < right and nums[left+1] == nums[left]:
        #             left += 1

        #         left += 1

        #     elif target < nums[right]:
        #         while left < right and nums[right-1] == nums[right]:
        #             right -= 1
                    
        #         right -= 1
            
        #     else:
        #         break

        # return False
        
        # Algorithm solution 4, O(logn) solution
        # Algorithm:
        # 1. Initialize two pointers, 'left' and 'right', where 'left' points to 
        #   the first element of the array and 'right' points to the last element 
        #   of the array.
        # 2. While 'left' is less than or equal to 'right', repeat steps 3 
        #   through 6:
        # 3. Compute the middle element of the array as 'mid' = (left + right) / 2.
        # 4. If the middle element is equal to the target, return 'true'.
        # 5. If the left half of the array is sorted, i.e., nums[left] <= nums[mid], 
        #   then check if the target is in the left half, i.e., nums[left] <= target < nums[mid], 
        #   and adjust the 'right' pointer accordingly.
        # 6. If the right half of the array is sorted, i.e., nums[mid] <= nums[right], 
        #   then check if the target is in the right half, i.e., nums[mid] < target <= nums[right], 
        #   and adjust the 'left' pointer accordingly.
        # 7. If the target is not found after the while loop, return 'false'.
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            
            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid - 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False
                
    

a = Solution()

print(a.search(nums = [2,5,6,0,0,1,2], target = 0))
print(a.search(nums = [2,5,6,0,0,1,2], target = 3))