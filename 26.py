# 26
# Remove Duplicates from Sorted Array
# Easy
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_duplicates(nums):
    # nums = set(nums)
    # return len(nums)
    return len(set(nums))

print(remove_duplicates([1,1,2]))
print(remove_duplicates([0,0,1,1,1,2,2,3,3,4]))