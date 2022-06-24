# LeetCode
# 2295
# Replace Elements in an Array
# https://leetcode.com/problems/replace-elements-in-an-array/

def array_change(nums, operations):
    for operation in operations:
        value_to_find = operation[0]
        value_to_replace = operation[1]
        # nums[index] += value
        nums[nums.index(value_to_find)] = value_to_replace
        # print(nums)
        # print(nums.index(value_to_find))
    
    return nums

# print(array_change([1, 2, 3], [[2, 3], [1, 5]]))
# print(array_change([1,2,4,6], [[1,3],[4,7],[6,1]]))
# print(array_change([1,2], [[1,3],[2,1],[3,2]]))

print(array_change())