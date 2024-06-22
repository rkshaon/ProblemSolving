# 290
# Word Pattern
# https://leetcode.com/problems/word-pattern/

def word_pattern(pattern, s):
    s = s.split(' ')

    if len(s) != len(pattern):
        return False

    words = {}
    seen_words = set()

    for index, c in enumerate(pattern):
        if c in words:
            if words[c] != s[index]:
                return False
        else:
            if s[index] in seen_words:
                return False
            
            words[c] = s[index]
            seen_words.add(s[index])

    return True


print(word_pattern(pattern = "abba", s = "dog cat cat dog"))
print(word_pattern(pattern = "abba", s = "dog cat cat fish"))
print(word_pattern(pattern = "aaaa", s = "dog cat cat dog"))
print(word_pattern(pattern = "abba", s = "dog dog dog dog"))