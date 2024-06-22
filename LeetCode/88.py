# LeetCode
# 88
# Merge Sorted Array
# Easy
# https://leetcode.com/problems/merge-sorted-array/

def merge(nums1, m, nums2, n):
    # temp = 
    for i in range(m, len(nums1)):
        # print(i)
        nums1[i] = nums2[i-m]

    nums1.sort()
    
    return nums1

print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))