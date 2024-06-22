# LeetCode
# 2011
# Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        
        for opt in operations:
            if opt == '++X' or opt == 'X++':
                x += 1
            elif opt == '--X' or opt == 'X--':
                x -= 1
        
        return x
        