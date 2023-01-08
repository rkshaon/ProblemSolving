# 242
# Valid Anagram
# https://leetcode.com/problems/valid-anagram/


def is_anagram(s: str, t: str):
    if len(s) != len(t):
        return False
    
    s_counts = {}
    t_counts = {}

    for c in s:
        if c in s_counts:
            s_counts[c] += 1
        else:
            s_counts[c] = 1
            
    for c in t:
        if c in t_counts:
            t_counts[c] += 1
        else:
            t_counts[c] = 1
            
    return s_counts == t_counts


print(is_anagram(s="anagram", t="nagaram"))
print(is_anagram(s="rat", t="car"))