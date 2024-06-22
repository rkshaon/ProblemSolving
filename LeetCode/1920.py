# LeetCode
# 1920
# Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans
        