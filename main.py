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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    step = next(sorter, None)