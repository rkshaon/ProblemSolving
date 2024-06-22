# LeetCode
# 1281
# Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        products = 1
        summation = 0
        
        str_n = str(n)
        
        for i in str_n:
            products *= int(i)
            summation += int(i)
        
        return products - summation
        