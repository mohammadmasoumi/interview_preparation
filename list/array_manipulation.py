# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for (a, b, k) in queries:
        arr[a - 1] += k
        if b <= len(arr):
            arr[b] -= k

    maxx = summ = 0
    for item in arr:
        summ += item

        if summ > maxx:
            maxx = summ

    return maxx
