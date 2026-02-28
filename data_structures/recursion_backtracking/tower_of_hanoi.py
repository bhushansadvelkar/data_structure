"""
Tower of Hanoi


Problem:
--------
Three rods (source, auxiliary, destination) and n disks of different sizes.
Start with all disks stacked on the source rod (largest at bottom, smallest on top).
Move all disks to the destination rod.

Rules:
- Only one disk can be moved at a time.
- Each move takes the top disk from one rod and places it on another.
- A disk cannot be placed on top of a smaller disk.

Examples:
---------
Example 1: n = 1
    Move disk 1 from A to C.

Example 2: n = 2
    Move disk 1 from A to B.
    Move disk 2 from A to C.
    Move disk 1 from B to C.

Example 3: n = 3
    (7 moves total)

Constraints:
------------
- 1 <= n <= 16 (typically)

Approach: Classic Recursion
--------------------------
- Base: n=1 → move disk 1 from source to dest.
- Recurrence:
  1. Move n-1 disks from source to aux (using dest as auxiliary).
  2. Move nth disk from source to dest.
  3. Move n-1 disks from aux to dest (using source as auxiliary).
- Total moves = 2^n - 1 (each disk moves once per level, 2^(n-1) times in its subtree).

Time Complexity: O(2^n)
    - We make 2^n - 1 moves; each move is O(1).

Space Complexity: O(n)
    - Recursion stack depth is n (we recurse n levels: n → n-1 → ... → 1).
"""

from data_structures.utils.test_utils import run_test


def tower_of_hanoi(n, source, aux, dest):
    """
    Print the moves to solve Tower of Hanoi for n disks.

    :type n: int - number of disks
    :type source: str - source rod (e.g. "A")
    :type aux: str - auxiliary rod (e.g. "B")
    :type dest: str - destination rod (e.g. "C")
    :rtype: None (or return list of moves if preferred)
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return

    tower_of_hanoi(n - 1, source, dest, aux)   # move n-1 from source to aux (using dest)
    print(f"Move disk {n} from {source} to {dest}")
    tower_of_hanoi(n - 1, aux, source, dest)   # move n-1 from aux to dest (using source)


if __name__ == "__main__":
    print("n=1:")
    tower_of_hanoi(1, "A", "B", "C")
    run_test(None, None, "n=1", compare=False, details="n=1, printed above")
    print("\nn=2:")
    tower_of_hanoi(2, "A", "B", "C")
    run_test(None, None, "n=2", compare=False, details="n=2, printed above")
    print("\nn=3:")
    tower_of_hanoi(3, "A", "B", "C")
    run_test(None, None, "n=3", compare=False, details="n=3, printed above")
