# 73
# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

def set_zeros(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()

    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.add(x)
                cols.add(y)
    
    for x in range(m):
        for y in range(n):
            if x in rows or y in cols:
                matrix[x][y] = 0
    
    return matrix


print(set_zeros(matrix = [[1,1,1],[1,0,1],[1,1,1]]))
print(set_zeros(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))