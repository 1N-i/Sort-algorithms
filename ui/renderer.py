import pygame
max_bar_height = 500
def renderer(surface, nums, id1=None, id2=None, green_id=-1):
    if min(nums) < 0:
        ground_level = 600
    else:
        ground_level = 1200

    y_zero = ground_level // 2
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
            color = (255, 0, 0) #Red
        elif i <= green_id:
            color = (0, 255, 0) #Green
        else:
            color = (255, 255, 255) #White

        pygame.draw.rect(surface, color, (x, y, width, height))