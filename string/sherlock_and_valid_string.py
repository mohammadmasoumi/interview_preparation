"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-
preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
"""
# !/bin/python3

import os
from collections import Counter


# Complete the isValid function below.
def isValid(s):
    repeatation = Counter(Counter(s).values())

    if len(repeatation) == 1 or len(repeatation) == 0:
        return "YES"

    elif len(repeatation) == 2:
        key1, key2 = repeatation.keys()
        if repeatation[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0):
            return "YES"
        elif repeatation[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0):
            return "YES"
        else:
            return "NO"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
