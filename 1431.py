# LeetCode
# 1431
# Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        max_candies = max(candies)
        
        for n in candies:
            if n + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result

        # return [True if n + extra_candies >= max_candies else False for n in candies]
        # another solution which takes more time.