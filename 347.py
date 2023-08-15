# 347
# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
# Medium
# Array, Hash Table, Divide and Conquer, Sorting, 
# Heap (Priority Queue), Bucket Sort, Counting, 
# Quickselect

from typing import List


# Time Complexity O(klogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for n, c in count.items():
            freq[c].append(n)
            
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

                if len(result) == k:
                    return result



print(Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(Solution().topKFrequent(nums = [1], k = 1))
