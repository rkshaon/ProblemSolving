# LeetCode
# 31
# Next Permutation
# https://leetcode.com/problems/next-permutation
# Medium
# Array, Two Pointer



from typing import List



class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n == 1:
            return
        
        i = 1
        lastInc = -1

        # Finding peak of the last Ascending Order
        while i < n:
            if nums[i] > nums[i - 1]:
                lastInc = i
            i += 1
        
        # Check if Array is in Descending Order
        if lastInc == -1:
            for i in range(int(n/2)):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
            
            return
        
        # Find the element in the range (nums[lastInc-1] to nums[lastInc]) to the right
        index = lastInc

        for i in range(lastInc, n):
            if nums[i] > nums[lastInc-1] and nums[i] < nums[index]:
                index = i
        
        nums[lastInc-1], nums[index] = nums[index], nums[lastInc-1]

        nums[lastInc:] = sorted(nums[lastInc:])

        return nums