def find_rotation_count(arr):
    min_elem, min_idx = 10000000, -1

    for idx, element in enumerate(arr):
        if element < min_elem:
            min_elem = element
            min_idx = idx

    return min_idx


def find_rotation_count2(arr):
    if len(arr) == 1:
        return 0

    middle = len(arr) // 2

    # 4,5,[1],2,3
    if arr[middle] < arr[middle - 1]:
        return middle

    # 3,4,[5],1,2
    # 1,2
    if middle + 1 < len(arr) and arr[middle + 1] < arr[middle]:
        return len(arr) - middle

    # 5,1,2,3,4
    if middle + 1 < len(arr) and arr[middle + 1] > arr[middle]:
        return find_rotation_count2(arr[:middle + 1])

    return find_rotation_count2(arr[middle:])


if __name__ == '__main__':
    arr =list( map(int, input().split(',')))

    print(find_rotation_count(arr=arr))
    print(find_rotation_count2(arr=arr))
