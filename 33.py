# LeetCode
# 33. Search in Rotated Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    # This is a solution, but with runtime complexity O(log n) which is not appropriate.
    if target not in nums:
        return -1

    return nums.index(target)


print(search(nums = [4,5,6,7,0,1,2], target = 0))
print(search(nums = [4,5,6,7,0,1,2], target = 3))
print(search(nums = [1], target = 0))