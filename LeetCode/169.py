# 169
# Majority Element
# https://leetcode.com/problems/majority-element/description/
# Easy

def majorityElement(nums):
    if not nums:
        return None
    
    if len(nums) == 1:
        return nums[0]
    
    counts = {}

    for n in nums:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    
    max_count = 0
    majority_element = None

    for n, c in counts.items():
        if c > max_count:
            max_count = c
            majority_element = n

    return majority_element


print(majorityElement(nums=[3,2,3]))
print(majorityElement(nums=[2,2,1,1,1,2,2]))