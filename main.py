from algorithms_generator.bubble_sort_generator import bubbleSortGenerator

from utils.data_generator import generateData
from ui.renderer import renderer
import pygame

pygame.init()
surface = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

nums = generateData(100, "totally_random", False)
sorter = bubbleSortGenerator(nums)

running = True
while running:
    for event in pygame.event.get(): #checks if the window should close
        if event.type == pygame.QUIT:
            running = False

    surface.fill((30, 30, 30))
    step = next(sorter, None)
    if step is not None:
        nums, id1, id2 = step
        renderer(surface, nums, id1, id2)
    else:
        #Future animation for when it's sorted
        renderer(surface, nums)

    pygame.display.flip()
    clock.tick(180) #Bigger value = Faster

pygame.quit()