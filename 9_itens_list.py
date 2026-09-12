from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.bubble_sort import bubbleSort
from algorithms.selection_sort import selectionSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort

import time #Calculate the time of each algorithm

#Functions list
algorithms = [iCantBelieveItCanSort,
              bubbleSort,
              selectionSort,
              insertionSort,
              mergeSort
              ]

#Same list for every algorithm
main_nums = [5, 4, 8, 1, 3, 2, 9, 6, 7]

print("Algorithms:               |         Time          | Result:")
print("--------------------------+-----------------------+----------------------------")
for algo in algorithms:
    nums = main_nums.copy()

    start = time.perf_counter()
    result = algo(nums)
    end = time.perf_counter()

    run_time = end - start

    print(f"{algo.__name__:<25} | {run_time * 1000000:^8.2f} microseconds | {result}")