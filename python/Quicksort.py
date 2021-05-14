# My attempt at Quicksort
# Exploring recursion in algorithms

import time
import random

def Quicksort(left, right, array):
    # print(array)
    if right - left <= 0:
        return
    
    pivot = Partition(left, right, array)

    Quicksort(left, pivot - 1, array)
    Quicksort(pivot + 1, right, array)

def Partition(left, right, array):
    # print("Starting partition")
    pivot = right
    right -= 1

    while True:
        while array[left] < array[pivot]:
            # print("Moving left")
            left += 1

        while array[right] > array[pivot]:
            # print("Moving right")
            right -= 1

        if left >= right:
            # print("Swapping pivot")
            Swap(left, pivot, array)
            break
        else:
            # print("Swapping pointers")
            # print(f"Left: {left} Right: {right}")
            # print(f"Left val: {array[left]} Right val: {array[right]} Pivot val: {array[pivot]}")
            Swap(left, right, array)
            left += 1

    return left


def Swap(left, pivot, array):
    hold = array[left]
    array[left] = array[pivot]
    array[pivot] = hold

def AverageCase(size):
    array = []
    for _ in range(size):
        array.append(random.randint(0, 100000))

    print(f"Random array is: {array}")

    start = time.perf_counter()
    Quicksort(0, size - 1, array)
    end = time.perf_counter()

    print(f"Sorted array: {array}")

    return end - start


if __name__ == "__main__":
    # array = [0, 5, 2, 1, 6, 3]
    # print(f"Array is: {array}")
    # Quicksort(0, len(array) - 1, array)
    # print(f"Sorted: {array}")

    time_qs = AverageCase(1000)
    print(f"Quicksort took {time_qs} seconds.")