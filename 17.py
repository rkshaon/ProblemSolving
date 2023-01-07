# 17
# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Medium

def letterCombinations(digits: str):
    if not digits:
        return []
    
    letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    combinations = [c for c in letters[digits[0]]]

    for d in digits[1:]:
        combinations = [comb + c for comb in combinations for c in letters[d]]
    
    return combinations


print(letterCombinations(digits=''))
print(letterCombinations(digits='23'))