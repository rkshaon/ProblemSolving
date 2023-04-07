# LeetCode
# 66. Plus One
# Easy
# https://leetcode.com/problems/plus-one/

def plus_one(digits):
    # Simple solution
    # num = int(''.join(map(str, digits))) + 1
    # digits = [int(digit) for digit in str(num)]
    # return digits
    # Complex solution
    return [int(digit) for digit in str(int(''.join(map(str, digits)))+1)]


print(plus_one([1,2,3]))