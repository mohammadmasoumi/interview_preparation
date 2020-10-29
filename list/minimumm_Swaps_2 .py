"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. You need to find the minimum number of swaps
required to sort the array in ascending order.

For example, given the array  we perform the following steps:

i   arr                     swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.

@see: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-
preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays
"""


# !/bin/python3


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # [4, 3, 1, 2]
    idx = 0
    num_swapped = 0

    while (True):
        if idx == len(arr):
            return num_swapped

        candidate = arr[idx]  # idx=0, candidate=4

        # print(f"DEBUG: candidate: {candidate}, idx: {idx}")
        if idx == candidate - 1:
            idx += 1
            continue

        swap_cost, swap_candidate_index = 100000, idx + 1
        for index, item in enumerate(arr[idx + 1:]):
            total_cost = abs(item - 1 - idx) + abs(candidate - 2 - index - idx)

            if total_cost < swap_cost:
                swap_cost = total_cost
                swap_candidate_index = idx + index + 1

        arr[idx], arr[swap_candidate_index] = arr[swap_candidate_index], arr[idx]
        num_swapped += 1


if __name__ == '__main__':
    # res = minimumSwaps(4, 3, 1, 2])
    res = minimumSwaps([2, 3, 4, 1, 5])
    print(res)
