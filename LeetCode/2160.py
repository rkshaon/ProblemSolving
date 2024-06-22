# LeetCode
# 2160
# Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        arr = [int(val) for val in str(num)]
        arr.sort()
        a, b, c, d = arr
        return (a + b) * 10 + c + d

print(Solution.minimumSum(Solution, 2932))