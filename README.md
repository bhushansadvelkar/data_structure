# Data Structures Practice

A Python package for practicing data structures and algorithms. Each topic is organized into its own subpackage for clear separation and easy navigation.

## Project Structure

```
data_structures/
├── arrays/                  # Array manipulation and problems
├── strings/                 # String algorithms and problems
├── sliding_window/          # Sliding window problems
├── stack/                   # Stack implementation and problems
├── linked_list/             # Linked list implementation and problems
├── binary_search/           # Binary search and its variants
├── trees/                   # Tree structures (BST, traversals, etc.)
├── heap/                    # Heap and priority queue
├── recursion_backtracking/  # Recursion and backtracking problems
├── dynamic_programming/     # DP problems and solutions
├── python_interview_questions/  # Python concepts (decorators, closures, …); see folder README
├── hashing/                 # Placeholder package (no exercises yet)
├── queue/                   # Placeholder package (no exercises yet)
├── graphs/                  # Placeholder package (no exercises yet)
└── utils/                   # Helper functions and utilities
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

# Optional: numpy (used by python_interview_questions/numpy examples)
pip install -r requirements.txt
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

## Revision flowcharts

- **Recursion & backtracking:** [RECURSION_FLOWCHARTS.md](data_structures/recursion_backtracking/RECURSION_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Arrays:** [ARRAYS_FLOWCHARTS.md](data_structures/arrays/ARRAYS_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Binary search:** [BINARY_SEARCH_FLOWCHARTS.md](data_structures/binary_search/BINARY_SEARCH_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Dynamic programming:** [DYNAMIC_PROGRAMMING_FLOWCHARTS.md](data_structures/dynamic_programming/DYNAMIC_PROGRAMMING_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Graphs:** [GRAPH_FLOWCHARTS.md](data_structures/graphs/GRAPH_FLOWCHARTS.md) (placeholder until problems are added; folder is otherwise empty).
- **Hashing:** [HASHING_FLOWCHARTS.md](data_structures/hashing/HASHING_FLOWCHARTS.md) (placeholder until problems are added; folder is otherwise empty).
- **Heap:** [HEAP_FLOWCHARTS.md](data_structures/heap/HEAP_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Linked list:** [LINKED_LIST_FLOWCHARTS.md](data_structures/linked_list/LINKED_LIST_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Queue:** [QUEUE_FLOWCHARTS.md](data_structures/queue/QUEUE_FLOWCHARTS.md) (placeholder until problems are added; folder is otherwise empty).
- **Sliding window:** [SLIDING_WINDOW_FLOWCHARTS.md](data_structures/sliding_window/SLIDING_WINDOW_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Stack:** [STACK_FLOWCHARTS.md](data_structures/stack/STACK_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Strings** (`strings/`): [STRINGS_FLOWCHARTS.md](data_structures/strings/STRINGS_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).
- **Trees:** [TREES_FLOWCHARTS.md](data_structures/trees/TREES_FLOWCHARTS.md) (code + Mermaid for every exercise in that folder).

## Conventions

- Keep problems in the matching topic folder (`arrays`, `linked_list`, `dynamic_programming`, etc.).
- Prefer file names like `leetcode_<id>_<problem_name>.py` for LeetCode problems.
- Add a docstring with problem statement, examples, constraints, approach, and complexity.
- Add runnable tests under `if __name__ == "__main__":` using `run_test`.

## Requirements

- Python 3.8+
- Core exercises use the standard library only. `requirements.txt` lists optional packages (e.g. `numpy` for interview examples).
