# 217
# https://leetcode.com/problems/contains-duplicate/description/
# Easy
# Array, Hash Table, Sorting



from typing import List


# Previous accepted solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
        
#         for i in range(0, len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
            
#         return False

# Another solution
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True

#             hashset.add(n)
        
#         return False


# Another solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return False if len(set(nums)) == len(nums) else True

solution = Solution()

print(solution.containsDuplicate(nums=[1, 2, 3, 1]))
print(solution.containsDuplicate(nums=[1, 2, 3, 4]))
print(solution.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2]))