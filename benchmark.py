from algorithms.bubble_sort import bubbleSort
from algorithms.bucket_sort import bucketSort
from algorithms.cocktail_sort import cocktailSort
from algorithms.comb_sort import combSort
from algorithms.counting_sort import countingSort
from algorithms.double_selection_sort import doubleSelectionSort
from algorithms.gnome_sort import gnomeSort
#from algorithms.gravity_sort import gravitySort
from algorithms.heap_sort import heapSort
from algorithms.i_cant_believe_it_can_sort import iCantBelieveItCanSort
from algorithms.insertion_sort import insertionSort
from algorithms.merge_sort import mergeSort
from algorithms.odd_even_sort import oddEvenSort
from algorithms.pancake_sort import pancakeSort
from algorithms.python_sort import pythonSort
from algorithms.quick_sort import quickSort
from algorithms.radix_sort import radixSort
from algorithms.selection_sort import selectionSort
from algorithms.shell_sort import shellSort
#from algorithms.stooge_sort import stoogeSort
from algorithms.tim_sort import timSort

import time #Calculate the time of each algorithm
from random import randint

from utils.data_generator import generateData

algorithms = [ #Functions list
    bubbleSort,
    bucketSort,
    cocktailSort,
    combSort,
    countingSort,
    doubleSelectionSort,
    gnomeSort,
    #gravitySort,
    heapSort,
    iCantBelieveItCanSort,
    insertionSort,
    mergeSort,
    oddEvenSort,
    pancakeSort,
    pythonSort,
    quickSort,
    radixSort,
    selectionSort,
    shellSort,
    #stoogeSort,
    timSort
]

def run_benchmark(size, data_style, allow_negative):
    main_nums = generateData(size, data_style, allow_negative)
    results = {}

    for algo in algorithms:
        nums = main_nums.copy()

        try:
            start = time.perf_counter()
            result = algo(nums)

            end = time.perf_counter()
            run_time = end - start
            info_to_save = round(run_time * 1000, 2)

            #Verifies if it's truly sorted
            assert result == sorted(main_nums), f"{algo.__name__} sorted incorrectly\n"
        except Exception:
            info_to_save = "Recursion error"

        results[algo.__name__] = info_to_save

    return results

if __name__ == "__main__":
    results = run_benchmark(5000, "totally_random", True)
    for algo in results:
        print(f"{algo}: {results[algo]} ms")