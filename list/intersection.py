# non-distinct and sorted

def intersection(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    intersection_list = []
    i, j = 0, 0  # i -> arr1, j -> arr2

    while i != len_arr1 and j != len_arr2:
        a, b = arr1[i], arr2[j]

        if a == b:
            if len(intersection_list) > 0 and intersection_list[-1] == a:
                pass
            else:
                intersection_list.append(a)

            i += 1
            j += 1
        elif a > b:
            j += 1
        else:
            i += 1

    return intersection_list if len(intersection_list) != 0 else [-1]


if __name__ == '__main__':
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    arr2 = [3, 4, 5, 8, 10]

    print(intersection(arr1, arr2))
