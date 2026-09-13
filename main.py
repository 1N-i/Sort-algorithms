from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.bubble_sort import bubbleSort
from algorithms.selection_sort import selectionSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort
from algorithms.quick_sort import quickSort
from algorithms.heap_sort import heapSort
from algorithms.counting_sort import countingSort

import time #Calculate the time of each algorithm
from random import randint

#Functions list
algorithms = [iCantBelieveItCanSort,
              bubbleSort,
              selectionSort,
              insertionSort,
              mergeSort,
              quickSort,
              heapSort,
              countingSort
              ]

nums_size = [10, 1000, 5000]
for size in nums_size: #Same list for every algorithm
    main_nums = [randint(-size, size) for _ in range(size)] #Random list

    print("----------------------+----------------------+------------+")
    print(f"{"Algorithms:":^21} | {"Time:":^20} | {size:^4} itens |") #Display
    print("----------------------+----------------------+------------+")
    for algo in algorithms:
        nums = main_nums.copy()

        start = time.perf_counter()
        result = algo(nums)
        end = time.perf_counter()
        run_time = end - start

        assert result == sorted(main_nums), f"{algo.__name__} sorted incorrectly" #Verifies if it's truly sorted

        print(f"{algo.__name__:^21} | {run_time * 1000:^8.2f} miliseconds |")

    print(f"----------------------+----------------------+ \n")