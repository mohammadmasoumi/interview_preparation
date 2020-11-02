# code

import string


def is_special(char):
    if char in string.punctuation:
        return True

    return False


def special_array_reversal(my_string):
    i, j = 0, len(my_string) - 1

    reversed_string = [''] * len(my_string)

    while (i <= j):
        char_i, char_j = my_string[i], my_string[j]

        if is_special(char_i):
            reversed_string[i] = char_i
            i += 1
            continue

        if is_special(char_j):
            reversed_string[j] = char_j
            j -= 1
            continue

        reversed_string[i], reversed_string[j] = char_j, char_i
        j -= 1
        i += 1

    return ''.join(reversed_string)


if __name__ == '__main__':
    number = int(input())

    output = []
    for _ in range(number):
        output.append(special_array_reversal(input()))

    for item in output:
        print(item)
