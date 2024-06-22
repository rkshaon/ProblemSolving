# 3
# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Medium

def lengthOfLongestSubstring(s):
    sub_str = ""
    max_length = -1

    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    
    for c in list(s):
        current = "".join(c)

        if current in sub_str:
            sub_str = sub_str[sub_str.index(current) + 1:]
        
        sub_str = sub_str + "".join(c)

        max_length = max(len(sub_str), max_length)

    return max_length


print(lengthOfLongestSubstring(s = "abcabcbb"))
print(lengthOfLongestSubstring(s = "bbbbb"))
print(lengthOfLongestSubstring(s = "pwwkew"))


