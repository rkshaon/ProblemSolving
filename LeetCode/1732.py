# LeetCode
# 1732
# Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = [0]
        
        for i in range(len(gain)):
            altitude.append(altitude[i] + gain[i])
        
        return max(altitude)
        