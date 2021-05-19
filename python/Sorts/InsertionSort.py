# Program that tests out insertion sort.
# O(N^2 + N) algorithm at the worst case.
# Explores the idea of looking at the average case rather than only at the worst case.

import time
import random

def InsertionSort(array):
    print(f"Inital array: {array}")
    current = 1
    count = 1
    steps = 0

    while current <= len(array) - 1:
        hold = array[current]
        steps += 1

        gap, steps = Shift(hold, current, array, steps)
        array[gap] = hold
        steps += 1
        print(f"Passthrough {count}: {array}")

        current += 1
        count += 1

    print(f"Total steps: {steps}")

def Shift(hold, current, array, steps):
    if current == 0:
        return current, steps

    steps += 1
    if hold < array[current - 1]:
        array[current] = array[current - 1]
        steps += 1
        current -= 1
        return Shift(hold, current, array, steps)
    else:
        return current, steps

def WorstCase(size):
    desc = list(range(size))[::-1]
    start = time.perf_counter()
    InsertionSort(desc)
    end = time.perf_counter()
    return end - start

def AverageCase(size):
    array = []
    for i in range(size):
        array.append(random.randint(0, 100))
    
    print(f"Random array: {array}")

    start = time.perf_counter()
    InsertionSort(array)
    end = time.perf_counter()
    return end - start

def AverageCase2(array):
    start = time.perf_counter()
    InsertionSort(array)
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    InsertionSort([4, 2, 7, 1, 3])
    # print(f"Worst Case for 100 elements took {WorstCase(100)} seconds")
    # print(f"Average Case for 100 elements took {AverageCase(100)} seconds")
    pass