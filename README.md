# Data Structures Practice

A Python package for practicing data structures and algorithms. Each topic is organized into its own subpackage for clear separation and easy navigation.

## Project Structure

```
data_structures/
├── arrays/              # Array manipulation and problems
├── strings/             # String algorithms and problems
├── hashing/             # Hash tables and hash-based solutions
├── stack/               # Stack implementation and problems
├── queue/               # Queue implementation and problems
├── linked_list/         # Linked list implementation and problems
├── binary_search/       # Binary search and its variants
├── trees/               # Tree structures (BST, AVL, etc.)
├── heap/                # Heap and priority queue
├── graphs/              # Graph algorithms (BFS, DFS, etc.)
├── recursion_backtracking/  # Recursion and backtracking problems
├── dynamic_programming/ # DP problems and solutions
└── utils/               # Helper functions and utilities
```

## Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate (Unix/macOS)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install in editable mode (optional)
pip install -e .
```

## Usage

Add solution files to the appropriate topic folder and run them directly.
Most files include a small test harness via `run_test(...)` in `if __name__ == "__main__":`.

```bash
# Run a file directly
python3 data_structures/arrays/leetcode_1_two_sum.py
python3 data_structures/dynamic_programming/subset_sum.py
```

You can also import modules in your own scripts:

```python
# Import in your code
from data_structures.arrays import leetcode_1_two_sum
from data_structures.dynamic_programming import subset_sum
```

## Conventions

- Keep problems in the matching topic folder (`arrays`, `linked_list`, `dynamic_programming`, etc.).
- Prefer file names like `leetcode_<id>_<problem_name>.py` for LeetCode problems.
- Add a docstring with problem statement, examples, constraints, approach, and complexity.
- Add runnable tests under `if __name__ == "__main__":` using `run_test`.

## Requirements

- Python 3.8+
