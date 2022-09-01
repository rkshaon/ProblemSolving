# LeetCode
# 1528
# Shuffle String
# https://leetcode.com/problems/shuffle-string/

def restore_string(s, indices):
    temp_result = [None] * len(s)

    for i in range(len(s)):
        temp_result[indices[i]] = s[i]

    return ''.join(i for i in temp_result)

print(restore_string('codeleet', [4,5,6,7,0,2,1,3]))
print(restore_string('abc', [0,1,2]))