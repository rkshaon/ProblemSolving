# LeetCode
# 1313
# Decompress Run-Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/

# Solution 1
# Runtime: 122ms
# Memory Usage: 14.4MB

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                result.append(nums[i+1])
        
        return result

# Solution 2
# Runtime: 76ms
# Memory Usage: 14.3MB
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(0, len(nums), 2):
            result += [nums[i+1] for j in range(nums[i])]
        
        return result