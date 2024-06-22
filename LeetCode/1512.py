# LeetCode
# 1512
# Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        
        for i in range(0, (len(nums) - 1)):
            for j in range(i + 1, len(nums)):
                if i < j and nums[i] == nums[j]:
                    good_pairs += 1
        
        return good_pairs
        