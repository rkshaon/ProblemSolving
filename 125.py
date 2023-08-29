# 125
# Valid Palindrome
# Easy
# https://leetcode.com/problems/valid-palindrome/description/
# Two Pointers, String


# Solution 1
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         new_s = ""

#         for c in s:
#             if c.isalnum():
#                 new_s += c.lower()
        
#         return new_s == new_s[::-1]
    


# Solution 2: Two pointer solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.isAlphaNum(s[left]):
                left += 1
            
            while left < right and not self.isAlphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1
        
        return True
    

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

print(Solution().isPalindrome(s = "A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(s = "race a car"))
print(Solution().isPalindrome(s = "rac a car"))