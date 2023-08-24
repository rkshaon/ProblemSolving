# 36
# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Medium
# Array, Hash Table, Matrix

from typing import List
import collections



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # columns
        rows = collections.defaultdict(set) # rows
        squares = collections.defaultdict(set) # square, key = (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3), (c // 3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3), (c // 3)].add(board[r][c])
        
        return True



print(Solution().isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
                
print(Solution().isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))