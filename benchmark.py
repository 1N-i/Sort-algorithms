from algorithms.bubble_sort import bubbleSort
from algorithms.bucket_sort import bucketSort
from algorithms.counting_sort import countingSort
from algorithms.heap_sort import heapSort
from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort
from algorithms.python_sort import pythonSort
from algorithms.quick_sort import quickSort
from algorithms.radix_sort import radixSort
from algorithms.selection_sort import selectionSort
from algorithms.shell_sort import shellSort
from algorithms.tim_sort import timSort

import time #Calculate the time of each algorithm
from random import randint

from utils.data_generator import generateData

algorithms = [ #Functions list
    bubbleSort,
    bucketSort,
    countingSort,
    heapSort,
    iCantBelieveItCanSort,
    insertionSort,
    mergeSort,
    pythonSort,
    quickSort,
    radixSort,
    selectionSort,
    shellSort,
    timSort
]

def run_benchmark(size, data_style, allow_negative):
    main_nums = generateData(size, data_style, allow_negative)
    results = {}

    for algo in algorithms:
        nums = main_nums.copy()

        start = time.perf_counter()
        result = algo(nums)
        end = time.perf_counter()
        run_time = end - start

        #Verifies if it's truly sorted
        assert result == sorted(main_nums), f"{algo.__name__} sorted incorrectly\n"
        results[algo.__name__] = round(run_time * 1000, 2)

    return results