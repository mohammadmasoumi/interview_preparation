"""
https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview
-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    res = 0
    current_char = s[0]
    for char in s[1:]:
        if char == current_char:
            res +=1
        else:
            current_char = char
    return res
