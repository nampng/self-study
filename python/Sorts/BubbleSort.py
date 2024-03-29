# Program to test out bubble sorting.
# O(N^2) algorithm. Simple sort.

import time
import random

def BubbleSort(array):
    if len(array) < 2:
        return

    print(f"Starting Array: {array}")

    end = len(array) - 1
    left = 0
    right = 1

    count = 1
    steps = 0

    swapped = False

    while True:
        if array[left] > array[right]:
            Swap(left, right, array)
            steps += 2
            swapped = True
        else:
            steps += 1
            swapped = False
        if right == end:
            print(f"Passthrough {count}: {array}")
            if swapped == False or end == 1:
                break
            
            end -= 1
            left = 0
            right = 1
            count += 1
        else:
            left += 1
            right += 1
    
    print(f"Total passthroughs: {count}")
    print(f"Total steps: {steps}")

def Swap(left, right, array):
    hold = array[left]
    array[left] = array[right]
    array[right] = hold

def WorstCase(size):
    array = list(range(size))
    desc = array[::-1]
    start = time.perf_counter()
    BubbleSort(desc)
    end = time.perf_counter()
    return end - start

def AverageCase(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 100))
    
    print(f"Random array: {array}")

    start = time.perf_counter()
    BubbleSort(array)
    end = time.perf_counter()
    return end - start

def AverageCase2(array):
    start = time.perf_counter()
    BubbleSort(array)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    # BubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    WorstCase(1000)