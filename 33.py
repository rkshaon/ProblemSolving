# LeetCode
# 33. Search in Rotated Sorted Array
# Medium
# Array, Binary Search
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search(nums, target):
    # This is a solution, but with runtime complexity O(log n) which is not appropriate.
    # if target not in nums:
    #     return -1

    # return nums.index(target)
    
    # O(log n) solution
    n = len(nums)
    left, right = 0, n-1

    # find the index of the smallest element
    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    # set the bounds for the binary search
    if target <= nums[-1]:
        left, right = left, n - 1
    else:
        left, right = 0, left - 1

    # perform binary search
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search(nums = [4,5,6,7,0,1,2], target = 0))
print(search(nums = [5,6,7,0,1,2,4], target = 0))
print(search(nums = [4,5,6,7,0,1,2], target = 3))
print(search(nums = [1], target = 0))