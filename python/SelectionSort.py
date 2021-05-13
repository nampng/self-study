# Program that tests out selection sort.
# O(N^2 / 2) ==> O(N^2) algorithm. Faster than Bubble.

import time
import random

def SelectionSort(array):
    start = 0
    end = len(array) - 1
    lowest = start
    current = start
    steps = 0
    passthrough = 1
    print(f"Starting array: {array}")
    while start != end -1:
        if current == end:
            Swap(lowest, start, array)
            print(f"Passthrough {passthrough}: {array}")
            start += 1
            lowest = start
            current = start
            passthrough += 1

        if array[lowest] > array[current]:
            lowest = current

        steps += 1
        current += 1

    print(f"Total steps: {steps}")

def Swap(lowest, start, array):
    hold = array[start]
    array[start] = array[lowest]
    array[lowest] = hold

def WorstCase(size):
    desc = list(range(size))[::-1]
    start = time.perf_counter()
    SelectionSort(desc)
    end = time.perf_counter()
    return end - start

def AverageCase(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 100))
    
    print(f"Random array: {array}")

    start = time.perf_counter()
    SelectionSort(array)
    end = time.perf_counter()
    return end - start

def AverageCase2(array):
    start = time.perf_counter()
    SelectionSort(array)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    SelectionSort([0, 6, 2, 8, 5, 7, 10])
    # WorstCase(1000)
