# LeetCode
# 121
# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            sell_price = prices[i]
            
            if sell_price - min_price > profit:
                profit = sell_price - min_price
            
            if sell_price < min_price:
                min_price = sell_price
        
        return profit
        