from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.bubble_sort import bubbleSort
from algorithms.selection_sort import selectionSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort

import time #Calculate the time of each algorithm
from random import randint

#Functions list
algorithms = [iCantBelieveItCanSort,
              bubbleSort,
              selectionSort,
              insertionSort,
              mergeSort
              ]

nums_size = [10, 5000]
for size in nums_size: #Same list for every algorithm
    main_nums = [randint(1, size) for _ in range(size)] #Random list

    print("----------------------+----------------------+------------+")
    print(f"{"Algorithms:":^21} | {"Time:":^20} | {size:^4} itens |") #Display
    print("----------------------+----------------------+------------+")
    for algo in algorithms:
        nums = main_nums.copy()

        start = time.perf_counter()
        result = algo(nums)
        end = time.perf_counter()
        run_time = end - start

        print(f"{algo.__name__:^21} | {run_time * 1000:^8.2f} miliseconds |")

    print(f"----------------------+----------------------+ \n")