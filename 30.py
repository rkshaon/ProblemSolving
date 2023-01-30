# 30
# Substring with Concatenation of All Words
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# Hard

import itertools
import re

def findSubstring(s, words):
    positions = []
    words = list(itertools.permutations(words))
    final_words = [''.join(w) for w in words]

    for word in final_words:
        positions.extend([m.start() for m in re.finditer(word, s)])
    # for word in final_words:
    #     if word in s:
    #         # positions.append(s.find(word))
    
    return list(set(positions))


print(findSubstring(s = "barfoothefoobarman", words = ["foo","bar"]))
print(findSubstring(s = "wordgoodgoodgoodbestword", words = ["word","good","best","good"]))
# Output: [8, 8]
# Result: [8]
print(findSubstring(s = "foobarfoobar", words = ["foo","bar"]))
# Output: [0,3]
# Result: [0,3,6]
print(findSubstring(s = "aaa", words = ["a","a"]))
# Output: [0]
# Result: [0,1]