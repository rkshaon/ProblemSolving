# LeetCode
# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Medium
# Array, Backtracking


from typing import List



class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(index, current, total):
            if total == target:
                results.append(current.copy())
                return
            
            if index >= len(candidates) or total > target:
                return
            
            current.append(candidates[index])
            backtrack(index, current, total + candidates[index])
            
            current.pop()
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)

        return results


a = Solution()

print(a.combinationSum(candidates = [2,3,6,7], target = 7))
print(a.combinationSum(candidates = [2,3,5], target = 8))
print(a.combinationSum(candidates = [2], target = 1))