# LeetCode
# 238
# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

def product(nums):
    result = []

    # for i in range(0, len(nums)):
    #     p = 1

    #     for j in range(0, len(nums)):            
    #         if i != j:
    #             p *= nums[j]
                
    #     result.append(p)
    for i in range(0, len(nums)):
        print(nums[~i])

    return result

print(product([1,2,3,4]))
print(product([-1,1,0,-3,3]))