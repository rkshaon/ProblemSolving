# LeetCode
# 1
# Two Sum
# https://leetcode.com/problems/two-sum/

# Solution 1
# Time complexity: O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
# Solution 2
# Time complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        
        for i in range(len(nums)):
            result = target - nums[i]
            
            if result in hash_map and hash_map[result] != i:
                return [i, hash_map[result]]
        