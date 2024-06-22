# LeetCode
# 13
# Roman to Integer

def romanToInt(s: str) -> int:
    ROMAN_VALUE = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,}
    ROMAN_MAP = {"I": 1, "V": 5, "X": 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    n = len(s)
    num = ROMAN_MAP[s[n - 1]]
    return num
    return n


print(romanToInt("MCMXCIV"))
