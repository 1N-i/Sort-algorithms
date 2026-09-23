import pygame
max_bar_height = 500
ground_level = 600
def renderer(surface, nums, id1=None, id2=None):
    bar_width = 800 / len(nums)
    max_val = max(nums)
    for i in range(len(nums)):
        x = i * bar_width
        width = bar_width

        val = nums[i]
        bar_height = (max_bar_height * val) / max_val
        height = bar_height
        y = ground_level - bar_height

        if i == id1 or i == id2:
            color = (255, 0, 0) # Vermelho
        else:
            color = (255, 255, 255) # Branco

        pygame.draw.rect(surface, color, (x, y, width, height))