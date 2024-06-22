# 1347
# Minimum Number of Steps to Make Two Strings Anagram
# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# Medium

from collections import Counter

def min_steps(s, t):
    c1, c2 = Counter(s), Counter(t)

    # result = [value for key, value in c2.items()]
    # print(result)
    n = 0

    for c in c2:
        # print(c, c2[c])
        if c in c1:
            print('if')
            print(c1[c], c2[c])
            # n += c1[c] - c2[c]
            n += c2[c] - c1[c]
        else:
            print('else')
            n += c2[c]

    return n
    # sorted_s = sorted(s)
    # sorted_t = sorted(t)

    # # print(sorted_s)
    # # print(sorted_t)

    # counter = 0

    # # for x in range(len(sorted_s)):
    # #     if sorted_s[x] != sorted_t[x]:
    # #         counter += 1

    # dict_s = {}
    # dict_t = {}

    # for x in sorted_s:
    #     if x in dict_s:
    #         dict_s[x] += 1
    #     else:
    #         dict_s[x] = 1
    
    # for y in sorted_t:
    #     if y in dict_t:
    #         dict_t[y] += 1
    #     else:
    #         dict_t[y] = 1
    
    # # print(dict_s)
    # # print(dict_t)
    # for x, y in zip(dict_s, dict_t):
    #     print(x, y)

    # return counter


print(min_steps(s = "bab", t = "aba"))
# print(min_steps(s = "leetcode", t = "practice"))