from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.bubble_sort import bubbleSort
from algorithms.selection_sort import selectionSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort
from algorithms.quick_sort import quickSort
from algorithms.heap_sort import heapSort
from algorithms.counting_sort import countingSort
from algorithms.radix_sort import radixSort
from algorithms.python_sort import pythonSort
from algorithms.bucket_sort import bucketSort
from algorithms.shell_sort import shellSort
from algorithms.tim_sort import timSort

import time #Calculate the time of each algorithm
from random import randint

from utils.data_generator import generateData

algorithms = [ #Functions list
    iCantBelieveItCanSort,
    bubbleSort,
    selectionSort,
    insertionSort,
    mergeSort,
    quickSort,
    heapSort,
    countingSort,
    radixSort,
    pythonSort,
    bucketSort,
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

        assert result == sorted(main_nums), f"{algo.__name__} sorted incorrectly\n" #Verifies if it's truly sorted
        results[algo.__name__] = round(run_time * 1000, 2)

    return results