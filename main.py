from algorithms_generator.bubble_sort_generator import bubbleSortGenerator
from algorithms_generator.bucket_sort_generator import bucketSortGenerator
from algorithms_generator.counting_sort_generator import countingSortGenerator
#from algorithms_generator.heap_sort import heapSort
from algorithms_generator.i_cant_believe_it_can_sort_generator import iCantBelieveItCanSortGenerator
#from algorithms_generator.insertion_sort import insertionSort
#from algorithms_generator.merge_sort import mergeSort
#from algorithms_generator.python_sort import pythonSort
#from algorithms_generator.quick_sort import quickSort
#from algorithms_generator.radix_sort import radixSort
#from algorithms_generator.selection_sort import selectionSort
#from algorithms_generator.shell_sort import shellSort

from utils.data_generator import generateData
from ui.renderer import renderer
import pygame

pygame.init()
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


#Functions list
algorithms = [                      #clock.tick(60) value
    bubbleSortGenerator,            #180
    bucketSortGenerator,            #30
    countingSortGenerator,          #45
    #heapSortGenerator,             #
    iCantBelieveItCanSortGenerator, #480
    #insertionSortGenerator,        #
    #mergeSortGenerator,            #
    #pythonSortGenerator,           #
    #quickSortGenerator,            #
    #radixSortGenerator,            #
    #selectionSortGenerator,        #
    #shellSortGenerator             #
]


#("already_sorted", "reverse_sorted", "totally_random", "nearly_sorted")
nums = generateData(100, "totally_random", True) #(size, style, allow_negatives)
algo = countingSortGenerator(nums)
green_id = -1

running = True
while running:
    for event in pygame.event.get(): #checks if the window should close
        if event.type == pygame.QUIT:
            running = False

    surface.fill((30, 30, 30))
    step = next(algo, None)
    if step is not None:
        nums, id1, id2 = step
        renderer(surface, nums, id1, id2)
        clock.tick(45) #Bigger value = Faster
    else:
        clock.tick(120)
        if green_id < len(nums):
            green_id += 1
        renderer(surface, nums, None, None, green_id)

    pygame.display.flip()

pygame.quit()