# 205
# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

def is_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s1_map = {}
    s2_map = {}

    for c1, c2 in zip(s1, s2):
        # print('c1, c2: ', c1, c2)
        if c1 in s1_map:
            # print(s1_map[c1], c2)
            if s1_map[c1] != c2:
                return False
        else:
            s1_map[c1] = c2

        if c2 in s2_map:
            # print(s2_map[c2], c1)
            if s2_map[c2] != c1:
                return False
        else:
            s2_map[c2] = c1

    return True

print(is_isomorphic(s1='egg', s2='add'))
print(is_isomorphic(s1='foo', s2='bar'))
print(is_isomorphic(s1='title', s2='paper'))