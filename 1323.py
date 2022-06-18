# LeetCode
# 1323
# Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        
        for i in range(len(num)):
            if num[i] == '6':
                num = num[:i] + '9' + num[i + 1:]
                break
        
        return int(num)
            