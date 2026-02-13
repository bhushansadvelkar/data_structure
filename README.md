# Data Structures Practice

A Python package for practicing data structures and algorithms. Each topic is organized into its own subpackage for clear separation and easy navigation.

## Solution Diagrams

**[View pictorial representations of solution approaches →](docs/APPROACH_DIAGRAMS.md)**

Flowcharts and diagrams showing how each problem was solved. Renders on GitHub.

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

Add your solution files to the appropriate package and run them directly or import:

```python
# Run a module directly
python -m data_structures.arrays.two_sum

# Import in your code
from data_structures.arrays import ...
from data_structures.stack import ...
```

## Requirements

- Python 3.8+
