# LeetCode
# 350
# Intersection of Two Arrays II
# Easy
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import Counter


def insertion(nums1, nums2):
    result = []
    c = Counter(nums1)

    print(c)

    for n in nums2:
        # print(n)
        # print(c[n])
        # print('n-value-from-n2 ', n, ' in-n1 ', c[n])
        if c[n] > 0:
            result.append(n)
            c[n] -= 1
    # for n in nums1:
    #     if n in nums2:
    #         result.append(n)

    return result

print(insertion(nums1 = [1,2,2,1], nums2 = [2,2]))
print(insertion(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))