# LeetCode
# 2194
# Cells in a Range on an Excel Sheet

def cell_in_range(s):
    ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 
        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    result = []

    cell_start = s.split(":")[0]
    cell_end = s.split(":")[1]

    col_start = ALPHABET.index(cell_start[0])
    col_end = ALPHABET.index(cell_end[0])

    row_start = int(cell_start[1:])
    row_end = int(cell_end[1:])

    for x in range(col_start, col_end+1):
        for y in range(row_start, row_end+1):
            result.append(ALPHABET[x] + str(y))

    return result

print(cell_in_range("K1:L2"))
print(cell_in_range("A1:F1"))