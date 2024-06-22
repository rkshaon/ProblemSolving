# LeetCode
# 1221
# Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/


class Solution:
    def balancedStringSplit(s: str):
        count = 0
        balance = 0

        for c in s:
            if c == 'L':
                balance += 1
            else:
                balance -= 1
            

            if balance == 0:
                count += 1
        
        return count


string = "RLRRLLRLRL"
print(Solution.balancedStringSplit(s=string))