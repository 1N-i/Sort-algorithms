# 🔀 Python Sorting Algorithms & Benchmarks

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)

A clean, modular Python repository designed to implement, understand, and benchmark various sorting algorithms from scratch, comparing algorithmic efficiency.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Repository Structure](#-repository-structure)
- [Implemented Algorithms](#-implemented-algorithms)
  - [Quadratic Algorithms - O(n²)](#1-quadratic-algorithms---on2)
  - [Logarithmic / Divide & Conquer Algorithms - O(n log n)](#2-logarithmic--divide--conquer-algorithms---on-log-n)
  - [Non-Comparison / Linear Algorithms - O(n + k)](#3-non-comparison--linear-algorithms---on--k)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)

---

## 🛠 Technologies
- **Python 3.x**: Core algorithm implementations and execution environment.
- **Time Module (`time.perf_counter`)**: High-precision timing used for performance benchmarking.
- **Random Module**: Generates randomized integer datasets for benchmark tests.

## ✨ Features
- **From-Scratch Implementations**: Every sorting algorithm is built independently to focus on conceptual clarity and algorithmic logic.
- **Automated Benchmarking Harness**: Centralized runner executing tests across dataset sizes of 10, 1,000, and 5,000 random elements.
- **Terminal Table Output**: Renders timing comparative tables directly in the console.
- **Modular & Scalable**: Designed with decoupled algorithm modules to seamlessly support future sorting algorithms.

## 📁 Repository Structure
* `algorithms/`: Directory containing individual modules for each sorting algorithm.
* `main.py`: Centralized benchmark runner using `time.perf_counter()` to execute algorithms across multiple dataset sizes (10, 1,000, and 5,000 random elements) and render clean formatted table outputs in the terminal.

## 🧮 Implemented Algorithms

### 1. Quadratic Algorithms - $O(n^2)$
* **I Can't Believe It Can Sort**: An unusually simple quadratic exchange sort using two full nested loops.
* **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
* **Selection Sort**: In-place comparison algorithm that repeatedly finds the minimum element from the unsorted region and places it at the beginning.
* **Insertion Sort**: Builds the final sorted array one item at a time by inserting unsorted elements into their correct position.
* **Shell Sort**: An optimization of insertion sort that compares elements separated by a decreasing gap sequence, significantly reducing element movement before finishing with a final gap-1 insertion pass.

### 2. Logarithmic / Divide & Conquer Algorithms - $O(n \log n)$
* **Merge Sort**: Divide and conquer algorithm that splits the array in half recursively, sorts each half, and merges them back together.
* **Quick Sort**: Divide and conquer algorithm utilizing a pivot element (with dedicated handling for duplicate values via equal buckets) to partition the array recursively.
* **Heap Sort**: In-place comparison sort using a complete binary tree structure (Max-Heap) and a `heapify` process to repeatedly extract the maximum element to the end of the array.
* **Python Sort (`python_sort`)**: Wrapper around Python's native `list.sort()` (Timsort), serving as the high-performance C-level baseline benchmark ($O(n \log n)$).

### 3. Non-Comparison / Linear Algorithms - $O(n + k)$
* **Counting Sort**: A non-comparison integer sorting algorithm that counts the frequency of distinct elements to calculate their exact output positions, operating in linear time $O(n + k)$.
* **Radix Sort**: A non-comparison integer sorting algorithm that processes numbers digit by digit from least to most significant position using counting sort as a stable subroutine, operating in $O(d \cdot (n + k))$ time.
* **Bucket Sort**: A distribution-based algorithm that divides input elements into several uniformly distributed buckets, individually sorts each bucket (often using Insertion Sort), and concatenates the results into a single sorted array.

## 🚀 How to Run

To run the automated benchmark harness and compare execution times across all algorithms, execute the following command:

```bash
python benchmark.py
```

## 🔮 Future Improvements
- [X] Add non-comparison sorting algorithms (**Counting Sort**, **Radix Sort**, **Bucket Sort**).
- [ ] Support custom input distributions (Ex: nearly sorted, reverse sorted, duplicate-heavy datasets).
- [ ] Add execution visualization and complexity graph rendering.
