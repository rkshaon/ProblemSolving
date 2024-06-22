# LeetCode
# 1572
# Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/submissions/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        start = 0
        end = len(mat) - 1
        result = 0
        
        for m in mat:
            if start == end:
                result += m[start]
            else:
                result += m[start] + m[end]
            
            start += 1
            end -= 1
        
        return result
        