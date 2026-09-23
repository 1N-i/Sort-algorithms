import random
def generateData(size, style, allow_negatives):
    if allow_negatives:
        min_val, max_val = -(size // 2), -(size // 2) + size
    else:
        min_val, max_val = 1, size + 1

    data = list(range(min_val, max_val))
    if style == "already_sorted":
        pass
        
    elif style == "reverse_sorted":
        data = data[::-1]
        
    elif style == "totally_random":
        random.shuffle(data)
        
    elif style == "nearly_sorted":
        swaps = max(1, int(size * 0.05))
        for _ in range(swaps):
            i1 = random.randint(0, size - 1)
            i2 = random.randint(0, size - 1)
            data[i1], data[i2] = data[i2], data[i1]

    return data