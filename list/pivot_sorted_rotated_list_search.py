def pivot_sorted_rotated_search(arr, element):
    # 3,4,5,1,2
    pivot_idx = find_pivot(arr)

    if pivot_idx == -1:
        return binary_search(arr, element)

    # 3,4,5,1,2 , pivot=2, element=3
    if arr[pivot_idx] == element:
        return pivot_idx

    if arr[0] < element < arr[pivot_idx]:
        return binary_search(arr[:pivot_idx], element)

    return binary_search(arr[pivot_idx:], element) + pivot_idx


def find_pivot(arr):
    # 1
    if len(arr) == 1:
        return -1

    middle = len(arr) // 2

    # 3,4,5,1,2
    if middle + 1 < len(arr) and arr[middle] > arr[middle + 1]:
        return middle

    # 4,5,1,2,3
    if arr[middle - 1] > arr[middle]:
        return middle - 1

    # 5,1,2,3, 4
    if middle + 1 < len(arr) and arr[middle] < arr[middle + 1]:
        return find_pivot(arr[:middle + 1])

    return find_pivot(arr[middle:])


def binary_search(arr, element):
    if len(arr) == 1:
        return -1

    middle = len(arr) // 2

    if arr[middle] == element:
        return middle

    if arr[middle] < element:
        return binary_search(arr[middle + 1:], element)

    return binary_search(arr[:middle], element)


if __name__ == '__main__':
    arr = list(map(int, input().split(',')))
    element = int(input())
    print(pivot_sorted_rotated_search(arr, element))
