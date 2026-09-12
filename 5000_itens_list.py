from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.bubble_sort import bubbleSort
from algorithms.selection_sort import selectionSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort

import time #Calculate the time of each algorithm
import random

#Functions list
algorithms = [iCantBelieveItCanSort,
              bubbleSort,
              selectionSort,
              insertionSort,
              mergeSort
              ]

#Same list for every algorithm
main_nums = [random.randint(1, 10000) for _ in range(5000)]

print("Algorithms:               |         Time         |")
print("--------------------------+----------------------+")
for algo in algorithms:
    nums = main_nums.copy()

    start = time.perf_counter()
    result = algo(nums)
    end = time.perf_counter()

    run_time = end - start

    print(f"{algo.__name__:<25} | {run_time * 1000:^8.2f} miliseconds |")