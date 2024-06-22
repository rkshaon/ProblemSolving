# LeetCode
# 1342
# Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            
            step += 1
        
        return step