# LeetCode
# 1365
# How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(0, len(nums)):
            c = 0
            for j in range(0, len(nums)):
                if i != j and nums[i] > nums[j]:
                    c += 1
            
            result.append(c)
        
        return result