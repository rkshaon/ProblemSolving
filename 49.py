# 49
# Group Anagrams
# https://leetcode.com/problems/group-anagrams/


# My own solution
def group_anagrams(strs):
    anagrams = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))

        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]

    return anagrams.values()


# ChatGPT solution
# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # Create a defaultdict to store the anagrams
#         anagrams = defaultdict(list)

#         # Iterate through the list of strings
#         for s in strs:
#             # Sort the characters of the string
#             sorted_str = ''.join(sorted(s))
#             # Add the original string to the list of anagrams for the sorted string
#             anagrams[sorted_str].append(s)

#         # Return the values of the defaultdict
#         return anagrams.values()

print(group_anagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams(strs = [""]))
print(group_anagrams(strs = ["a"]))