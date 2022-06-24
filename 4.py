# LeetCode
# Problem 4: Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

def find_median(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    
    if len(nums) % 2 == 0:
        return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    else:
        return nums[len(nums) // 2]

result = find_median([1, 2], [3, 4])

print(result)