from algorithms_generator.bubble_sort_generator import bubbleSortGenerator

from utils.data_generator import generateData
from ui.renderer import renderer
import pygame

pygame.init()
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#("already_sorted", "reverse_sorted", "totally_random", "nearly_sorted")
nums = generateData(100, "already_sorted", True) #(size, style, allow_negatives)
algorithm = bubbleSortGenerator(nums)
green_id = -1

running = True
while running:
    for event in pygame.event.get(): #checks if the window should close
        if event.type == pygame.QUIT:
            running = False

    surface.fill((30, 30, 30))
    step = next(algorithm, None)
    if step is not None:
        nums, id1, id2 = step
        renderer(surface, nums, id1, id2)
    else:
        if green_id < len(nums):
            green_id += 1
        renderer(surface, nums, None, None, green_id)

    pygame.display.flip()
    clock.tick(180) #Bigger value = Faster

pygame.quit()