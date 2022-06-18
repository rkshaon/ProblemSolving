# LeetCode
# 1678
# Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        command = command.replace("()", "o")
        command = command.replace("(al)", "al")
        
        return command