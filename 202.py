# 202
# Happy Number
# https://leetcode.com/problems/happy-number/

def is_happy(n):
    seen = set()

    while n not in seen:
        seen.add(n)
        n = sum(int(c)**2 for c in str(n))
    
    return n == 1


print(is_happy(n=19))
print(is_happy(n=1))
print(is_happy(n=9))