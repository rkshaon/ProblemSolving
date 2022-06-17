# LeetCode
# 771
# Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        return sum(s in jewels_set for s in stones)