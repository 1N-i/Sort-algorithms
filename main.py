from algorithms_generator.bubble_sort_generator import bubbleSortGenerator
from algorithms_generator.bucket_sort_generator import bucketSortGenerator
from algorithms_generator.counting_sort_generator import countingSortGenerator

from utils.data_generator import generateData
from ui.renderer import renderer
import pygame

pygame.init()
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

algorithms = [
    bubbleSortGenerator,
    bucketSortGenerator,
    countingSortGenerator
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
    else:
        if green_id < len(nums):
            green_id += 1
        renderer(surface, nums, None, None, green_id)

    pygame.display.flip()
    clock.tick(60) #Bigger value = Faster

pygame.quit()