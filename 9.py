# LeetCode
# 9
# Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        
        return False
        