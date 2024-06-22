# 438
# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

def find_anagrams(s, p):
    indexs = []
    length_of_p = len(p)
    length_of_s = len(s)
    sorted_p = ''.join(sorted(p))

    for x in range(length_of_s - length_of_p + 1):
        if sorted_p == ''.join(sorted(s[x:x+length_of_p])):
            indexs.append(x)
        
    return indexs


print(find_anagrams(s = "cbaebabacd", p = "abc"))
print(find_anagrams(s = "abab", p = "ab"))