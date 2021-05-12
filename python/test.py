# This script imports other modules for testing.

import BubbleSort
import SelectionSort

if __name__ == "__main__":
    time_bs = BubbleSort.WorstCase(10)
    time_ss = SelectionSort.WorstCase(10)

    print(f"Bubble Sort took {time_bs} seconds")
    print(f"Selection Sort took {time_ss} seconds")