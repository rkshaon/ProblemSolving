# 166
# Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/
# Medium

def fractionToDecimal(numerator: int, denominator: int):
    if denominator == 0:
        return ''
        
    if numerator == 0:
        return '0'
        
    sign = ''
        
    if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
        sign = '-'
        
    numerator = abs(numerator)
    denominator = abs(denominator)

    integer_part = numerator // denominator
    remainder = numerator % denominator

    if remainder == 0:
        return sign + str(integer_part)
        
    fractional_part = ''
    hash_table = {}
    index = 0

    while remainder != 0:
        if remainder in hash_table:
            index = hash_table[remainder]

            fractional_part = fractional_part[:index] + '(' + fractional_part[index:] + ')'
                
            break
            
        hash_table[remainder] = index
        index += 1

        numerator = remainder * 10
        fractional_part += str(numerator // denominator)
        remainder = numerator % denominator
        
    return sign + str(integer_part) + '.' + fractional_part


    


print(fractionToDecimal(numerator=4, denominator=333))
print(fractionToDecimal(numerator=1, denominator=2))
print(fractionToDecimal(numerator=2, denominator=1))