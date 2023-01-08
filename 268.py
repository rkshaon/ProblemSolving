# 268
# Missing Number
# https://leetcode.com/problems/missing-number/

def missing_number(nums):
    nums_list_in_range = [n for n in range(0, len(nums)+1)]

    return list(set(nums_list_in_range) - set(nums))[0]

    # single line solution
    return list(set(n for n in range(0, len(nums)+1)) - set(nums))[0]


print(missing_number(nums=[3, 0, 1]))
print(missing_number(nums=[0, 1]))
print(missing_number(nums=[9,6,4,2,3,5,7,0,1]))