#!/bin/python3

from collections import defaultdict


# Complete the makeAnagram function below.

def makeAnagram(a, b):
    a_dict = defaultdict(int)
    b_dict = defaultdict(int)

    for char in a:
        a_dict[char] += 1

    for char in b:
        b_dict[char] += 1

    keys = set(a_dict.keys()).union(b_dict.keys())

    return sum([abs(a_dict[key] - b_dict[key]) for key in keys])
