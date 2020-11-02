#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    count = 0

    for idx, char in enumerate(s):
        sub_string = ''
        inner_idx = idx
        while inner_idx < len(s):
            sub_string += char

            # if len(sub_string) == 1 or :
            #     inner_idx += 1
            #     count += 1

            # elif


if __name__ == '__main__':

    # n = int(input())
    # s = input()
    result = substrCount(10, 'aaaada')
    print(result)
