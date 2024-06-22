#!/bin/python3

# Easy
# Implementation

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#


def chocolateFeast(n, c, m):
    print(n, c, m)


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()
#         n = int(first_multiple_input[0])
#         c = int(first_multiple_input[1])
#         m = int(first_multiple_input[2])
#         result = chocolateFeast(n, c, m)
#         fptr.write(str(result) + '\n')

#     fptr.close()
if __name__ == '__main__':
    with open('HackerRank/input.txt', 'r') as fptr:
        t = int(fptr.readline().strip())

        results = []
        for t_itr in range(t):
            first_multiple_input = fptr.readline().rstrip().split()

            n = int(first_multiple_input[0])
            c = int(first_multiple_input[1])
            m = int(first_multiple_input[2])

            result = chocolateFeast(n, c, m)
            results.append(result)

    with open('HackerRank/output.txt', 'w') as fptr:
        for result in results:
            fptr.write(str(result) + '\n')
