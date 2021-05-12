# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 3
# Description: The following program provide practice with binary search operations 


import random
import time
from static_array import *


# ------------------- PROBLEM 1 - -------------------------------------------


def binary_search(arr: StaticArray, target: int) -> int:
    """
    This binary_search takes in an ordered list and a target and performs
    a binary search on said list for the traget. If found, it returns the 
    index otherwise it returns -1. This function can take anything so long 
    as it is ordered either from smallets to biggest or vice versa. Runtime 
    is O(log N).
    """
    size = arr.size()
    if size == 0:
        return -1
    if arr.get(0) < arr.get(size - 1): # ordered from smallest to biggest
        start = 0
        end = size - 1
        while start <= end:
            mid = (start + end)//2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1 
    else: # ordered from biggest to smallest
        start = 0
        end = size - 1
        while start <= end:
            mid = (start + end)//2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) < target:
                end = mid - 1
            else:
                start = mid + 1
    return -1

# ------------------- PROBLEM 2 - -------------------------------------------


def binary_search_rotated(arr: StaticArray, target: int) -> int:
    """
    This function takes in a sorted array that is rotated an unknown number 
    of times, and a target value. If the target is found in the array it returns
    the index otherwise it returns -1. This function has a runtime complexity of
    O(log N).
    """
    size = arr.size()
    if size == 0:
        return -1
    if arr.get(0) <= arr.get(size - 1): # no duplicates guaranteed so start = end only when size = 1
        start = 0                       # the case where the sorted list is not rotated 
        end = size - 1
        while start <= end:  
            mid = (start + end)//2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    # gets the real index where the value is the smallest in the array
    # assumes that a rotation has occured, otherwise will fail
    # Also the fact that the array is sorted in ascending order helps 
    start = 0
    end = size - 1
    rotatesAt = -1
    done = False 
    while not done:
        mid = (start + end)//2
        if (arr.get(mid) <= arr.get(start) and arr.get(mid) <= arr.get(end)): # if the current val is smaller than value at start and the value at end
            if mid != 0 and arr.get(mid - 1) <= arr.get(mid):   # if the val before current val is even smaller then keep going in the binary search
                end = mid - 1
            else:                                               # otherwise returns the index where rotation occurs
                rotatesAt = mid
                done = True
        elif arr.get(mid) > arr.get(end):
            start = mid + 1
        else:
            end = mid - 1 
    # breaks the array into two sections and checks for the target value in the section which it falls underneath in. 
    if arr.get(rotatesAt) == target:
        return rotatesAt 
    elif target > arr.get(size - 1) and target <= arr.get(rotatesAt - 1): 
        start = 0
        end = rotatesAt - 1
        while start <= end:
            mid = (start + end)//2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    elif target > arr.get(rotatesAt) and target <= arr.get(size - 1):
        start = rotatesAt
        end = size - 1
        while start <= end:
            mid = (start + end)//2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    else:
        return -1


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":
    pass

    print('\n# problem 1 example 1')
    src = (-10, -5,)
    targets = (7, -10, 11, 0, 8, 1, -100, 100)
    arr = StaticArray(len(src))
    for i, value in enumerate(src):
        arr[i] = value
    print([binary_search(arr, target) for target in targets])
    arr._data.reverse()
    print([binary_search(arr, target) for target in targets])


    print('\n# problem 1 example 2')
    """
    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]

    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]

    result, total_time = True, 0
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)

    arr._data.reverse()
    for target in targets:
        total_time -= time.time()
        answer = binary_search(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
    """


    print('\n# problem 2 example 1')
    test_cases = (
        ((6, 8, 12, 20, 0, 2, 5), 0),
        ((6, 8, 12, 20, 0, 2, 5), -1),
        ((1,), 1),
        ((1,), 0),
        ((-1,), 0),
    )
    result = []
    for src, target in test_cases:
        arr = StaticArray(len(src))
        for i, value in enumerate(src):
            arr[i] = value
        result.append((binary_search_rotated(arr, target)))
    print(*result)
    

    print('\n# problem 2 example 2')
    """
    src = [random.randint(-10 ** 7, 10 ** 7) for _ in range(5_000_000)]
    src = sorted(set(src))
    arr = StaticArray(len(src))
    arr._data = src[:]
    
    # add 20 valid and 20 (likely) invalid targets
    targets = [-10 ** 8, 10 ** 8]
    targets += [arr[random.randint(0, len(src) - 1)] for _ in range(20)]
    targets += [random.randint(-10 ** 7, 10 ** 7) for _ in range(18)]
    
    result, total_time = True, 0
    for target in targets:
        # rotate arr random number of steps
        pivot = random.randint(0, len(src) - 1)
        arr._data = src[pivot:] + src[:pivot]

        total_time -= time.time()
        answer = binary_search_rotated(arr, target)
        total_time += time.time()
        result &= arr[answer] == target if target in src else answer == -1
    print(result, total_time < 0.5)
    """

