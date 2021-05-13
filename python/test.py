# This script imports other modules for testing.

import BubbleSort
import SelectionSort
import InsertionSort

import random

if __name__ == "__main__":
    # time_bs = BubbleSort.WorstCase(10)
    # time_ss = SelectionSort.WorstCase(10)

    # print(f"Bubble Sort took {time_bs} seconds")
    # print(f"Selection Sort took {time_ss} seconds")

    array = []
    for x in range(1000):
        array.append(random.randint(0, 100000))

    time_bs = BubbleSort.AverageCase2(array)
    # time_ss = SelectionSort.AverageCase2(array)
    # time_is = InsertionSort.AverageCase2(array)

    print(f"Bubble Sort took {time_bs} seconds")
    # print(f"Selection Sort took {time_ss} seconds")
    # print(f"Insertion Sort took {time_is} seconds")