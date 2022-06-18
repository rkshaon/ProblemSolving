# LeetCode
# 1528
# Shuffle String
# https://leetcode.com/problems/shuffle-string/

def restore_string(s, indices):
    return ''.join(s[i] for i in indices)

print(restore_string('codeleet', [4,5,6,7,0,2,1,3]))