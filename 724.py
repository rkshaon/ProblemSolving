# 724
# Find Pivot Index

def pivotIndex(nums):
        pivot_index = -1
        
        for i in range(len(nums)):
            print(nums[i:], nums[:i])
            if sum(nums[i+1:]) == sum(nums[:i]):
                print(nums[i:], nums[:i])
                pivot_index = i
        
        return pivot_index

print(pivotIndex([1,7,3,6,5,6]))
# [-1,-1,0,0,-1,-1]