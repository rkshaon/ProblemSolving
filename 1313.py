# LeetCode
# 1313
# Decompress Run-Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                result.append(nums[i+1])
        
        return result

# nums = [1,2,3,4]

# def decompressList(nums):
#     result = []

#     for i in range(0, len(nums), 2):
#         for j in range(nums[i]):
#             result.append(nums[i+1])

#     return result

# print(decompressList(nums))