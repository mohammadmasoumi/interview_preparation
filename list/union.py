def union(arr1, arr2):
    size1, size2 = len(arr1), len(arr2)
    union_list = []

    i, j = 0, 0  # i -> size1, j -> size2

    while i != size1 and j != size2:
        a, b = arr1[i], arr2[j]

        if a > b:
            union_list.append(b)
            j += 1
        elif a < b:
            union_list.append(a)
            i += 1
        else:
            if len(union_list) > 0 and union_list[-1] == a:
                pass
            else:
                union_list.append(a)

            i += 1
            j += 1

    return union_list if len(union_list) else [-1]


if __name__ == '__main__':
    arr1 = [1, 2, 2, 3, 4, 5, 6, 7]
    arr2 = [4, 5, 6, 7, 8, 9, 9]

    print(union(arr1, arr2))
