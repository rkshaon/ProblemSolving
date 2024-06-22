# 128
# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Medium
# Array, Hash Table, Union Find

from typing import List



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            if (n-1) not in numSet:
                length = 0

                while (n+length) in numSet:
                    length += 1
                
                longest = max(length, longest)
        
        return longest
    


print(Solution().longestConsecutive(nums = [100,4,200,1,3,2]))
print(Solution().longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))