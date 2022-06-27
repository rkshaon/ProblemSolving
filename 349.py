# LeetCode
# 349
# Intersection of Two Arrays
# Easy
# https://leetcode.com/problems/intersection-of-two-arrays/

def insertion(nums1, nums2):
    result = []    
    nums1 = set(nums1)
    nums2 = set(nums2)

    for n in nums1:
        if n in nums2:
            result.append(n)

    return result

print(insertion(nums1 = [1,2,2,1], nums2 = [2,2]))
print(insertion(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))