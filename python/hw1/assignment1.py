# Course: CS261 - Data Structures
# Student Name: Elias Meshesha
# Assignment: 1
# Description: Programming practice with a series of problems.

import random
import string
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> ():
    """
    Given an instance of StaticArray that holds an array, the following function
    finds the max and min of the array and returns the two values as tuple.
    """
    min = arr.get(0)
    max = arr.get(0)
    size = arr.size()

    for index in range(size):
        if arr.get(index) > max:
            max = arr.get(index)
        elif arr.get(index) < min:
            min = arr.get(index)
    return min, max

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    Returns a new static array where its elements are similar to the current
    array except if the element is divisible by 3, it is set to "fizz", if the
    element is divisible by 5, it is set to "buzz", if it is divisible by both
    it is set to "fizzbuzz".
    """
    newArr = StaticArray(arr.size())

    for index in range(arr.size()):
        if arr.get(index) % 15 == 0:
            newArr.set(index, 'fizzbuzz')
        elif arr.get(index) % 3 == 0:
            newArr.set(index, 'fizz')
        elif arr.get(index) % 5 == 0:
            newArr.set(index, 'buzz')
        else:
            newArr.set(index, arr.get(index))

    return newArr


# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverses the current array by modifying the contents only
    """
    for index in range(arr.size()//2):
        temp = arr.get(index)
        arr.set(index, arr.get(arr.size() - 1 - index))
        arr.set(arr.size() - 1 - index, temp)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    A function that receives a StaticArray and an integer value (called
    steps). The function creates and returns a new StaticArray, where all
    elements are from the original array but their position has shifted
    right or left steps number of times. If steps is positive, elements
    are shifted right, else if steps is negative elements should be shifted left
    """
    newArr = StaticArray(arr.size())
    for index in range(arr.size()):
        newArr.set(index, arr.get(index))

    absSteps = abs(steps)
    quotient = absSteps//arr.size()
    rem = absSteps - quotient*arr.size()
    for index in range(newArr.size()):
        if steps > 0:
            newIndex = index + rem
            if newIndex >= newArr.size():
                newIndex -= newArr.size()
            newArr.set(newIndex, arr.get(index))
        elif steps < 0:
            newIndex = index - rem
            if newIndex < 0:
                newIndex += newArr.size()
            newArr.set(newIndex, arr.get(index))

    return newArr

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Receives two integers start and end. This function return an array that has
    all values between start and end (inclusive).
    """
    size = end - start
    if end >= start:
        size += 1
    else:
        size -= 1
    arr = StaticArray(abs(size))
    index = 0
    if end >= start:
        for num in range(start, end + 1, 1):
            arr.set(index, num)
            index += 1
    elif end < start:
        for num in range(start, end-1, -1):
            arr.set(index, num)
            index += 1

    return arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Receives a StaticArray and returns an integer that describes whether
    the array is sorted. The function will return 1 if the array is sorted
    in strictly ascending order, it will return 2 if the list is sorted in
    strictly descending order, Otherwise, it will return 0.
    """
    num = 0
    if arr.size() == 1:
        return 1
    if arr.get(0) > arr.get(1):
        for index in range(arr.size()):
            if index != arr.size() - 1:
                if arr.get(index) <= arr.get(index + 1):
                    return num
        num = 2
        return num
    else:
        for index in range(arr.size()):
            if index != arr.size() - 1:
                if arr.get(index) >= arr.get(index + 1):
                    return num
        num = 1
        return num

# ------------------- PROBLEM 7 - SA_SORT -----------------------------------


def sa_sort(arr: StaticArray) -> None:
    """
    A function that receives a StaticArray and sorts its content in
    non-descending order.
    """
    for index in range(1,arr.size()):
        val = arr.get(index)
        pos = index - 1
        while pos >= 0 and arr.get(pos) > val:
            arr.set(pos+1, arr.get(pos))
            pos-= 1
        arr.set(pos+1, val)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray where the elements are already
    in sorted order and returns a new StaticArray with duplicate values
    removed.
    """
    newSize = 1
    temp = arr.get(0)
    for index in range(1, arr.size()):
        if arr.get(index) != temp:
            newSize += 1
            temp = arr.get(index)

    newArr = StaticArray(newSize)
    newSize = 0
    temp = arr.get(newSize)
    newArr.set(newSize, temp)
    for index in range(1, arr.size()):
        if arr.get(index) != temp:
            newSize += 1
            temp = arr.get(index)
            newArr.set(newSize, temp)
    return newArr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------


def count_sort(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray and returns a new StaticArray
    with the same content sorted in non-ascending order
    """
    max, min = arr.get(0), arr.get(0)
    for index in range(1, arr.size()):
        if arr.get(index) > max:
            max = arr.get(index)
        elif arr.get(index) < min:
            min = arr.get(index)

    size = max - min
    if size >= 0:
        size += 1
    else:
        size -= 1
    dictionary = StaticArray(abs(size))
    for index in range(arr.size()):
        num = arr.get(index)
        i = num - min
        value = dictionary.get(i)
        if value is None:
            value = 0
        value +=1
        dictionary.set(i, value)

    cDictionary = StaticArray(abs(size))
    cDictionary.set(0,0)
    for index in range(1, dictionary.size()):
        num = cDictionary.get(index - 1)
        v = dictionary.get(index - 1)
        if v is None:
            v = 0
        num += v
        cDictionary.set(index, num)

    newArr = StaticArray(arr.size())
    for index in range(arr.size()):
        val = arr.get(index)
        key = val - min
        temp = cDictionary.get(key)
        newArr.set(arr.size() - 1 - temp, val)
        temp += 1
        cDictionary.set(key, temp)

    return newArr

# ------------------- PROBLEM 10 - SA_INTERSECTION --------------------------


def sa_intersection(arr1: StaticArray, arr2: StaticArray, arr3: StaticArray)-> StaticArray:
    """
    A function that receives three StaticArrays where the elements are
    already in sorted order and returns a new StaticArray with only
    those elements that appear in all three input arrays
    """
    size, index2, index3 = 0, 0, 0
    for index1 in range(arr1.size()):#(start1, end1 + 1):
        value1 = arr1.get(index1)
        if index2 != arr2.size(): value2 = arr2.get(index2)
        else: value2 = None
        if index3 != arr3.size(): value3 = arr3.get(index3)
        else: value3 = None
        while value2 is not None and value1 > value2 and index2 < arr2.size() - 1:
            index2 += 1
            value2 = arr2.get(index2)
        while value3 is not None and value1 > value3 and index3 < arr3.size() - 1:
            index3 += 1
            value3 = arr3.get(index3)
        if value1 == value2 and value1 == value3:
            size += 1
            index2 += 1
            index3 += 1
    if size == 0:
        newArr = StaticArray(1)
        newArr.set(0, None)
        return newArr
    newArr = StaticArray(size)
    index, index2, index3 = 0, 0, 0
    for index1 in range(arr1.size()):  # (start1, end1 + 1):
        value1 = arr1.get(index1)
        if index2 != arr2.size(): value2 = arr2.get(index2)
        else: value2 = None
        if index3 != arr3.size(): value3 = arr3.get(index3)
        else: value3 = None
        while value2 is not None and value1 > value2 and index2 < arr2.size() - 1:
            index2 += 1
            value2 = arr2.get(index2)
        while value3 is not None and value1 > value3 and index3 < arr3.size() - 1:
            index3 += 1
            value3 = arr3.get(index3)
        if value1 == value2 and value1 == value3:
            newArr.set(index, value1)
            index += 1
            index2 += 1
            index3 += 1
    return newArr

# ------------------- PROBLEM 11 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray where the elements are already
    in sorted order and returns a new StaticArray with squares of the values
    from the original array, sorted in non-descending order.
    """
    newArr = StaticArray(arr.size())
    indexAt0 = None
    prev = 0
    current = 0
    for index in range(arr.size()):
        i = index
        j = index - 1
        newArr.set(index, (arr.get(index))**2)
        if newArr.get(index) == 0:
            indexAt0 = index
        elif j >= 0 and arr.get(i) > 0 and arr.get(j) < 0:
            if arr.get(i) != 0 and arr.get(j) != 0:
                current = abs(arr.get(i))
                prev = abs(arr.get(j))
                if current > prev:
                    indexAt0 = j
                else:
                    indexAt0 = i

    if indexAt0 is None and arr.get(0) > 0:
        return newArr
    newNewArr = StaticArray(arr.size())
    if indexAt0 is None and arr.get(0) < 0:
        for index in range(arr.size()):
            val = newArr.get(index)
            newNewArr.set(arr.size() - 1 - index, val)
        return newNewArr
    backward = indexAt0 - 1
    forward = indexAt0 + 1
    newNewArr.set(0, newArr.get(indexAt0))

    for index in range(1, newArr.size()):
        if backward >= 0:
            val1 = newArr.get(backward)
        else:
            val1 = 18446744073709551615
        if forward < newArr.size():
            val2 = newArr.get(forward)
        else:
            val2 = 18446744073709551615
        if val1 < val2:
            value = val1
            backward -= 1
        else:
            value = val2
            forward += 1
        newNewArr.set(index, value)
    return newNewArr

# ------------------- PROBLEM 12 - ADD_NUMBERS ------------------------------


def add_numbers(arr1: StaticArray, arr2: StaticArray) -> StaticArray:
    """
    A function that receives two StaticArray, each representing a
    non-negative number, and returns a new StaticArray representing
    a sum of these two numbers. Arrays stores the number by having
    each element in the array represent an individual digit.
    """
    num1 = 0
    for index in range(arr1.size()):
        temp = arr1.get(index)
        num1*= 10
        num1+= temp
    num2 = 0
    for index in range(arr2.size()):
        temp = arr2.get(index)
        num2*= 10
        num2+= temp
    num3 = num1 + num2
    temp = 1
    size = 0
    factor = 10
    while temp != 0:
        temp = num3//factor
        factor*=10
        size += 1
    newArr = StaticArray(size)
    factor = 10
    for index in range(newArr.size()):
        rem = num3 % factor
        newArr.set(newArr.size() - 1 - index, rem)
        num3 = num3//factor
    return newArr


# ------------------- PROBLEM 13 - SPIRAL MATRIX -------------------------


def spiral_matrix(rows: int, cols: int, start: int) -> StaticArray:
    """
    A function that receives three integers (rows, cols, and start), then creates and
    returns a 2D matrix (represented as a StaticArray of StaticArrays). The returned matrix
    is filled with the integers that start from the provided start value and sequentially
    increase by 1 (if the start value is >= 0) or decrease by 1 (if the start value is < 0).
    Also if the start value is non-negative, the start value is placed in the upper right corner of the
    matrix, and all subsequent integers are placed in the matrix in a clockwise spiral order.
    When the start value is negative, the start value is placed in the lower left corner of the matrix,
    and all subsequent integers are placed in the matrix in a counterclockwise spiral order.
    """
    newArr = StaticArray(rows)
    for index in range(newArr.size()):
        newA = StaticArray(cols)
        newArr.set(index, newA)
    col, row = 0, 0
    if start >= 0:
        col = cols
        col -= 1
        while row != rows and newArr.get(row).get(col) is None:
            while row != rows and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start += 1
                row += 1
            col -= 1
            row -= 1
            while col >= 0 and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start += 1
                col -= 1
            row -= 1
            col += 1
            while row >= 0 and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start += 1
                row -= 1
            row += 1
            col += 1
            while col < cols and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start += 1
                col += 1
            col -= 1
            row += 1
    else:
        row = rows
        row -= 1
        while col < cols and newArr.get(row).get(col) is None:
            while col < cols and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start -= 1
                col += 1
            col -= 1
            row -= 1
            while row >= 0 and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start -= 1
                row -= 1
            row += 1
            col -= 1
            while col >= 0 and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start -= 1
                col -= 1
            row += 1
            col += 1
            while row != rows and newArr.get(row).get(col) is None:
                newArr.get(row).set(col, start)
                start -= 1
                row += 1
            col += 1
            row -= 1

    return newArr


# ------------------- PROBLEM 14 - TRANSFORM_STRING -------------------------


def transform_string(source: str, s1: str, s2: str) -> str:
    """
    A function that receives three strings (source, s1, and s2) and then
    returns a modified string of the same length as source. Modification
    follows rules below.
    1) If the character from the source string is present in s1, it should
       be replaced by the character at the same index in s2.
    2) Otherwise, if the character is:
        a) Uppercase letter -> replace with ' '
        b) Lowercase letter -> replace with '#'
        c) Digit -> replace with '!'
        d) Anything else -> replace with '='
    """
    str1 = StaticArray(len(s1))
    str2 = StaticArray(len(s2))
    for index in range(len(s1)):
        str1.set(index, s1[index])
    for index in range(len(s2)):
        str2.set(index, s2[index])
    myString = ""
    for num in range(len(source)):
        char = source[num]
        x = False
        i = 0
        for index in range(str1.size()):
            if char == str1.get(index):
                i = index
                x = True
        if char >= "a" and char <= "z" and x is False:
            myString += '#'
        elif char >= "A" and char <= "Z" and x is False:
            myString += " "
        elif char >= "0" and char <= "9" and x is False:
            myString += "!"
        elif x:
            myString += str2.get(i)
        else:
            myString += "="
    return myString


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(min_max(arr))


    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(min_max(arr))


    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(min_max(arr))


    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)


    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)


    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2**28, -2**31]:
        print(rotate(arr, steps), steps)
    print(arr)


    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3**14)
    rotate(arr, -3**15)
    print(f'Finished rotating large array of {array_size} elements')


    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-105, -99), (-99, -105)]
    for start, end in cases:
        print(start, end, sa_range(start, end))


    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print('Result:', is_sorted(arr), arr)


    print('\n# sa_sort example 1')
    test_cases = (
        [1, 10, 2, 20, 3, 30, 4, 40, 5],
        ['zebra2', 'apple', 'tomato', 'apple', 'zebra1'],
        [(1, 1), (20, 1), (1, 20), (2, 20)],
        [random.randint(-10**7, 10**7) for _ in range(5_000)]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        sa_sort(arr)
        print(arr if len(case) < 50 else 'Finished sorting large array')


    print('\n# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)


    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr if len(case) < 50 else 'Started sorting large array')
        result = count_sort(arr)
        print(result if len(case) < 50 else 'Finished sorting large array')


    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')


    print('\n# sa_intersection example 1')
    test_cases = (
        ([1, 2, 3], [3, 4, 5], [2, 3, 4]),
        ([1, 2], [2, 4], [3, 4]),
        ([1, 1, 2, 2, 5, 75], [1, 2, 2, 12, 75, 90], [-5, 2, 2, 2, 20, 75, 95]),
        ([-10, -1, 0, 5, 6, 8], [6, 7], [-10, -8, -8, -3, -1, -1, 1, 6, 8]),
        ([-8, -5, -2, 4, 4, 4, 7, 9], [-10, -9, -7, -5, -5, -3, -3, 7, 8, 9], [-5])
    )
    for case in test_cases:
        arr = []
        for i, lst in enumerate(case):
            arr.append(StaticArray(len(lst)))
            for j, value in enumerate(sorted(lst)):
                arr[i][j] = value
        print(sa_intersection(arr[0], arr[1], arr[2]))


    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
        [-3, -2, 1, 4],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)


    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10**9, 10**9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
    

    print('\n# add_numbers example 1')
    test_cases = (
        ([1, 2, 3], [4, 5, 6]),
        ([0], [2, 5]), ([0], [0]),
        ([2, 0, 9, 0, 7], [1, 0, 8]),
        ([9, 9, 9], [9, 9, 9, 9])
    )
    for num1, num2 in test_cases:
        n1 = StaticArray(len(num1))
        n2 = StaticArray(len(num2))
        for i, value in enumerate(num1):
            n1[i] = value
        for i, value in enumerate(num2):
            n2[i] = value
        print('Original nums:', n1, n2)
        print('Sum: ', add_numbers(n1, n2))


    print('\n# spiral matrix example 1')
    matrix = spiral_matrix(1, 1, 7)
    print(matrix)
    if matrix: print(matrix[0])
    matrix = spiral_matrix(3, 2, 12)
    if matrix: print(matrix[0], matrix[1], matrix[2])


    print('\n# spiral matrix example 2')
    def print_matrix(matrix: StaticArray) -> None:
        rows, cols = matrix.size(), matrix[0].size()
        for row in range(rows):
            for col in range(cols):
                print('{:4d}'.format(matrix[row][col]), end=' ')
            print()
        print()

    test_cases = (
        (4, 4, 1), (3, 4, 0), (2, 3, 10), (1, 2, 1), (1, 1, 42),
        (4, 4, -1), (3, 4, -3), (2, 3, -12), (1, 2, -42),
    )
    for rows, cols, start in test_cases:
        matrix = spiral_matrix(rows, cols, start)
        if matrix: print_matrix(matrix)


    print('\n# transform_strings example 1')
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')
    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
