# 242
# Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Hash Table, String, Sorting

# from typing import str

# New solution 1
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
        
#         for c in countS:
#             if countS[c] != countT.get(c, 0):
#                 return False
        
#         return True

# New solution 2
from collections import Counter
 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

solution = Solution()

print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))

# Previous Solution
# def is_anagram(s: str, t: str):
#     if len(s) != len(t):
#         return False
    
#     s_counts = {}
#     t_counts = {}

#     for c in s:
#         if c in s_counts:
#             s_counts[c] += 1
#         else:
#             s_counts[c] = 1
            
#     for c in t:
#         if c in t_counts:
#             t_counts[c] += 1
#         else:
#             t_counts[c] = 1
            
#     return s_counts == t_counts


# print(is_anagram(s="anagram", t="nagaram"))
# print(is_anagram(s="rat", t="car"))