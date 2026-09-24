import pygame
max_bar_height = 500
ground_level = 600
y_zero = ground_level // 2
def renderer(surface, nums, id1=None, id2=None):
    bar_width = 800 / len(nums)
    max_abs_val = max(abs(x) for x in nums)
    for i in range(len(nums)):
        x = i * bar_width
        width = bar_width

        val = nums[i]
        bar_height = (max_bar_height * val) / (2 * max_abs_val)
        if val > 0:
            height = bar_height
            y = y_zero - bar_height
        else:
            height = bar_height * -1
            y = y_zero

        if i == id1 or i == id2:
            color = (255, 0, 0) # Vermelho
        else:
            color = (255, 255, 255) # Branco

        pygame.draw.rect(surface, color, (x, y, width, height))