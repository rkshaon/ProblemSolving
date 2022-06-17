# LeetCode
# 1480
# Running Sum of 1d Array

class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        return nums