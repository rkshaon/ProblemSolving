# LeetCode
# 58. Length of Last Word
# Easy
# https://leetcode.com/problems/length-of-last-word/

def length_of_word(s):
    s = s.split(' ')
    new_list = [x for x in s if x != '']
    
    return len(new_list[-1])

print(length_of_word("Hello World"))
print(length_of_word("   fly me   to   the moon  "))