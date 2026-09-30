from algorithms_generator.bubble_sort_generator import bubbleSortGenerator
from algorithms_generator.bucket_sort_generator import bucketSortGenerator
from algorithms_generator.counting_sort_generator import countingSortGenerator
from algorithms_generator.heap_sort_generator import heapSortGenerator
from algorithms_generator.i_cant_believe_it_can_sort_generator import iCantBelieveItCanSortGenerator
from algorithms_generator.insertion_sort_generator import insertionSortGenerator
from algorithms_generator.merge_sort_generator import mergeSortGenerator
from algorithms_generator.tim_sort_generator import timSortGenerator
from algorithms_generator.quick_sort_generator import quickSortGenerator
from algorithms_generator.radix_sort_generator import radixSortGenerator
from algorithms_generator.selection_sort_generator import selectionSortGenerator
from algorithms_generator.shell_sort_generator import shellSortGenerator

from utils.data_generator import generateData
from ui.renderer import renderer
import pygame

from flask import Flask, request, jsonify
app = Flask(__name__, static_folder="./ui", static_url_path="")
@app.route("/api/render", methods=["POST"])
def route():
    data = request.get_json() #Captures the JSON send by fetch
    print("Received:", data)

    run_visualizer(data["algo"], data["size"], data["dataType"], data["allowNegative"])
    return jsonify({"status": "success"})

@app.route("/")
def index():
    return app.send_static_file("index.html")

def run_visualizer(algo_name, size, data_type, allow_negative):
    algorithms = {
        "bubble_sort": bubbleSortGenerator,
        "bucket_sort": bucketSortGenerator,
        "counting_sort": countingSortGenerator,
        "heap_sort": heapSortGenerator,
        "i_cant_believe_it_can_sort": iCantBelieveItCanSortGenerator,
        "insertion_sort": insertionSortGenerator,
        "merge_sort": mergeSortGenerator,
        "tim_sort": timSortGenerator,
        "quick_sort": quickSortGenerator,
        "radix_sort": radixSortGenerator,
        "selection_sort": selectionSortGenerator,
        "shell_sort": shellSortGenerator
    }

    pygame.init()
    surface = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    nums = generateData(size, data_type, allow_negative)
    algo = algorithms[algo_name](nums)
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
            clock.tick(120) #Speed the algorithm runs
        else:
            clock.tick(60) #Speed of the sorted animation
            if green_id < len(nums):
                green_id += 1
            renderer(surface, nums, None, None, green_id)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    app.run(debug=True)