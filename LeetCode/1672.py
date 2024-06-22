# 1672
# Richest Customer Wealth
# Easy
# https://leetcode.com/problems/richest-customer-wealth/

def maximum_wealth(accounts):
    max_wealth = 0

    for account in accounts:
        if sum(account) > max_wealth:
            max_wealth = sum(account)
    return max_wealth

print(maximum_wealth([[1,2,3],[3,2,1]]))
print(maximum_wealth([[1,5],[7,3],[3,5]]))