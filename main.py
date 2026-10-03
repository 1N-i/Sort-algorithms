from algorithms_generator.bubble_sort_generator import bubbleSortGenerator
from algorithms_generator.bucket_sort_generator import bucketSortGenerator
from algorithms_generator.counting_sort_generator import countingSortGenerator
from algorithms_generator.heap_sort_generator import heapSortGenerator
from algorithms_generator.i_cant_believe_it_can_sort_generator import iCantBelieveItCanSortGenerator
from algorithms_generator.insertion_sort_generator import insertionSortGenerator
from algorithms_generator.merge_sort_generator import mergeSortGenerator
from algorithms_generator.quick_sort_generator import quickSortGenerator
from algorithms_generator.radix_sort_generator import radixSortGenerator
from algorithms_generator.selection_sort_generator import selectionSortGenerator
from algorithms_generator.shell_sort_generator import shellSortGenerator
from algorithms_generator.tim_sort_generator import timSortGenerator

from utils.data_generator import generateData
from ui.renderer import renderer
import pygame


from flask import Flask, request, jsonify
app = Flask(__name__, static_folder="./ui", static_url_path="")
@app.route("/api/render", methods=["POST"])
def route():
    data = request.get_json() #Captures the JSON send by fetch
    print("Received:", data)

    run_visualizer(data["algo"], data["size"], data["dataType"], data["allowNegative"], data["speed"])
    return jsonify({"status": "success"})

@app.route("/")
def index():
    return app.send_static_file("index.html")

from benchmark import run_benchmark
@app.route("/api/benchmark", methods=["POST"])
def benchmark_route():
    data = request.get_json()
    results = run_benchmark(data["size"], data["dataType"], data["allowNegative"])
    return jsonify(results)


def run_visualizer(algo_name, size, data_type, allow_negative, speed):
    algorithms = {
        "bubble_sort": bubbleSortGenerator,
        "bucket_sort": bucketSortGenerator,
        "counting_sort": countingSortGenerator,
        "heap_sort": heapSortGenerator,
        "i_cant_believe_it_can_sort": iCantBelieveItCanSortGenerator,
        "insertion_sort": insertionSortGenerator,
        "merge_sort": mergeSortGenerator,
        "quick_sort": quickSortGenerator,
        "radix_sort": radixSortGenerator,
        "selection_sort": selectionSortGenerator,
        "shell_sort": shellSortGenerator,
        "tim_sort": timSortGenerator,
    }

    pygame.init()
    window_lenght = 800
    window_height = 600
    surface = pygame.display.set_mode((window_lenght, window_height))
    clock = pygame.time.Clock()

    nums = generateData(size, data_type, allow_negative)
    algo = algorithms[algo_name](nums)
    green_id = -1

    font = pygame.font.SysFont("arial", 28)
    text = font.render("Press SPACE to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(window_lenght // 2, 25))
    waiting = True
    while waiting:
        renderer(surface, nums, None, None)
        surface.blit(text, text_rect)
        clock.tick(60)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN: #Checks if the animation should start
                if event.key == pygame.K_SPACE:
                    waiting = False

    running = True
    while running:
        for event in pygame.event.get(): #Checks if the window should close
            if event.type == pygame.QUIT:
                running = False

        surface.fill((30, 30, 30))
        step = next(algo, None)
        if step is not None:
            nums, id1, id2 = step
            renderer(surface, nums, id1, id2)
            clock.tick(int(speed) * 5) #Speed the algorithm runs
        else:
            clock.tick(int(speed) * 5) #Speed of the sorted animation
            if green_id < len(nums):
                green_id += 1
            renderer(surface, nums, None, None, green_id)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    print("http://localhost:5000/")
    app.run(debug=True)