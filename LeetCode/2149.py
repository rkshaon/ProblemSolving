# 2149
# Rearrange Array Elements by Sign
# Medium
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        return nums