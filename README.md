# 📊 Sorting Algorithms Visualizer & Benchmark

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/flask-REST--API-black?style=for-the-badge&logo=flask)
![Pygame](https://img.shields.io/badge/pygame-visualization-green?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/javascript-ES6+-yellow?style=for-the-badge&logo=javascript)

A full-stack Python and Web application designed to visualize, benchmark, and compare 13 sorting algorithms in real time.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Implemented Algorithms](#-implemented-algorithms)
- [Repository Structure](#-repository-structure)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)

---

## 🛠 Technologies
- **Backend**: Python 3.x, Flask (REST API)
- **Visualization**: Pygame (Generator-driven animations)
- **Frontend**: HTML5, CSS3, JavaScript ES6 (Fetch API, Async DOM rendering)
- **Benchmarking**: High-precision timing via `time.perf_counter`

## ✨ Features
- **Interactive Web Interface**: Custom controls for dataset size, negative numbers flag, and data distribution types (Already sorted, Reverse sorted, Totally random, Nearly sorted).
- **Generator-Driven Animation**: Pygame visualizer uses Python `yield` generators to render array state transitions, element swaps, and a completion sweep without blocking execution.
- **Dynamic Web Benchmark**: Executes all algorithms against identical data configurations and returns a JSON response to construct a dynamic HTML benchmark table.

## 📊 Implemented Algorithms

### 1. Quadratic Algorithms — $O(n^2)$
- **I Can't Believe It Can Sort**: An unusually simple quadratic exchange sort using two full nested loops.
- **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps out-of-order pairs.
- **Selection Sort**: In-place comparison algorithm that repeatedly finds the minimum element and places it at the sorted partition.
- **Insertion Sort**: Builds the sorted array one item at a time by inserting unsorted elements into their correct position.
- **Shell Sort**: An optimization of insertion sort using decreasing gap sequences to move distant elements efficiently.

### 2. Logarithmic / Divide & Conquer Algorithms — $O(n \log n)$
- **Merge Sort**: Recursively splits the array in half, sorts each half, and merges them together.
- **Quick Sort**: Uses a pivot element to partition the array recursively into smaller and larger sub-arrays.
- **Heap Sort**: Converts the list into a Max-Heap binary tree to repeatedly extract the largest element.
- **Python Sort**: Native C-level `list.sort()` (Timsort) serving as the baseline benchmark.
- **Tim Sort**: Hybrid sorting algorithm combining Merge Sort and Insertion Sort designed for real-world data patterns.

### 3. Non-Comparison & Linear Algorithms — $O(n + k)$ / $O(d \cdot (n + k))$
- **Counting Sort**: Non-comparison algorithm counting element frequencies to determine exact positions in linear time.
- **Radix Sort**: Non-comparison algorithm processing numbers digit-by-digit using counting sort as a stable subroutine.
- **Bucket Sort**: Distributes elements into uniform buckets, sorts each individually, and concatenates the result.

## 📂 Repository Structure

```text
Sort-algorithms/
├── algorithms/                 # Pure algorithm implementations (for benchmarks)
│   ├── bubble_sort.py
│   ├── quick_sort.py
│   └── ...
├── algorithms_generator/       # Generator-based algorithm implementations (yielding steps for Pygame visualization)
│   ├── bubble_sort_generator.py
│   ├── quick_sort_generator.py
│   └── ...
├── ui/                         # Web frontend interface & Pygame graphics renderer
│   ├── index.html              # Dashboard controls & benchmark output section
│   ├── style.css               # Layout styling and UI components
│   ├── script.js               # Async Fetch API triggers and DOM manipulators
│   └── renderer.py             # Pygame canvas rendering logic (bars, swap highlights, green completion state)
├── utils/                      # Helper tools
│   └── data_generator.py       # Flexible data generation (Already sorted, Reverse sorted, Random, Nearly sorted)
├── main.py                     # Flask web server & Pygame application orchestrator
└── benchmark.py                # Performance measurement engine across all 13 algorithms
```

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install flask pygame
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Open in browser:**
   Navigate to `http://localhost:5000/`

## 🔮 Future Improvements
- [X] Support custom input distributions (already sorted, reverse sorted, totally random, nearly sorted).
- [X] Add execution visualization and benchmark time visualization.
- [ ] Add interactive range sliders for animation speed controls.
- [ ] Implement UI loading indicators ("Waiting for response...") during benchmark execution.
