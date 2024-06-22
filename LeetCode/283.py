# 283
# Move Zeroes
# https://leetcode.com/problems/move-zeroes
# Easy
# Array, Two Pointer



from typing import List



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            print(nums[i])
            # if nums[i] == 0:
            #     print('ZERO')
            #     nums[i], nums[i+1] = nums[i+1], nums[i]

            #     print(nums)

        return nums



print(Solution().moveZeroes(nums = [0,1,0,3,12]))