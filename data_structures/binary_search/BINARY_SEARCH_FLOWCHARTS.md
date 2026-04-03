# Binary search — revision flowcharts

Each section shows **code from the repo first**, then **Mermaid** (and ASCII where helpful). Mermaid renders on GitHub and in previews with a Mermaid extension.

**Contents:** [704 Binary Search](#1-leetcode_704_binary_searchpy) · [35 Search Insert](#2-35_search_insert_positionpy) · [First / Last Occurrence](#3-first_and_last_occurance_of_elementpy) · [Floor](#4-find_floor_of_elementpy) · [Descending Array](#5-binary_serch_reverse_sorted_arraypy) · [Rotation Count](#6-no_of_times_sorted_array_is_rotatedpy) · [153 Min Rotated](#7-leetcode_153_find_minimum_in_rotated_sorted_arraypy) · [744 Next Letter](#8-leetcode_744_find_letter_greater_than_targetpy) · [2529 Pos / Neg Count](#9-leetcode_2529_max_count_of_positive_negative_integerpy)

---

## 1. `leetcode_704_binary_search.py`

### Code

```python
class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return -1
```

### Flowchart

```mermaid
flowchart TD
    A[start=0, end=n-1] --> W{start <= end?}
    W -->|no| R[return -1]
    W -->|yes| M[mid = start+end // 2]
    M --> E{nums mid == target?}
    E -->|yes| F[return mid]
    E -->|no| G{nums mid > target?}
    G -->|yes| L[end = mid - 1]
    G -->|no| H[start = mid + 1]
    L --> W
    H --> W
```

**Facts:** Time O(log n), space O(1).

---

## 2. `35_search_insert_position.py`

### Code

```python
class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l
```

### Flowchart

```mermaid
flowchart TD
    A[l=0, r=n-1] --> W{l <= r?}
    W -->|no| Z[return l insert index]
    W -->|yes| M[mid = l + r-l // 2]
    M --> E{nums mid == target?}
    E -->|yes| F[return mid]
    E -->|no| G{nums mid > target?}
    G -->|yes| X[r = mid - 1]
    G -->|no| Y[l = mid + 1]
    X --> W
    Y --> W
```

**Facts:** When the loop exits, `l` is the first index where `nums[i] >= target` (insert position). Time O(log n), space O(1).

---

## 3. `first_and_last_occurance_of_element.py`

### Code

```python
class Solution(object):
    def firstandLastOccuranceofNumber(self, nums, target):
        start = 0
        end = len(nums) - 1
        first = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                first = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        start = 0
        end = len(nums) - 1
        last = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                last = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        if first == -1:
            return [-1, -1]

        return [first, last]
```

### Flowchart — pass 1 (leftmost index of `target`)

```mermaid
flowchart TD
    F1[start=0, end=n-1, first=-1] --> FW{start <= end?}
    FW -->|no| DONE1[Pass 1 done]
    FW -->|yes| FM[mid]
    FM --> FE{nums mid == target?}
    FE -->|yes| FY[first = mid, end = mid - 1]
    FE -->|no| FG{nums mid > target?}
    FG -->|yes| FL[end = mid - 1]
    FG -->|no| FS[start = mid + 1]
    FY --> FW
    FL --> FW
    FS --> FW
```

### Flowchart — pass 2 (rightmost index of `target`)

```mermaid
flowchart TD
    L1[Reset start=0, end=n-1, last=-1] --> LW{start <= end?}
    LW -->|no| CHK{first == -1?}
    LW -->|yes| LM[mid]
    LM --> LE{nums mid == target?}
    LE -->|yes| LY[last = mid, start = mid + 1]
    LE -->|no| LG{nums mid > target?}
    LG -->|yes| LL[end = mid - 1]
    LG -->|no| LS[start = mid + 1]
    LY --> LW
    LL --> LW
    LS --> LW
    CHK -->|yes| R1[return -1, -1]
    CHK -->|no| R2[return first, last]
```

**ASCII**

```
First:  on == target → remember index, search LEFT  (end = mid - 1).
Last:   on == target → remember index, search RIGHT (start = mid + 1).
```

**Facts:** Two passes, each O(log n); space O(1).

---

## 4. `find_floor_of_element.py`

### Code

```python
class Solution(object):
    def findFloorementinArray(self, nums, target):
        start = 0
        end = len(nums) - 1
        result = -1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                result = nums[mid]
                start = mid + 1

        return result
```

### Flowchart

```mermaid
flowchart TD
    A[result = -1] --> W{start <= end?}
    W -->|no| R[return result]
    W -->|yes| M[mid]
    M --> Q{nums mid >= target?}
    Q -->|yes| L[end = mid - 1]
    Q -->|no| S[result = nums mid, start = mid + 1]
    L --> W
    S --> W
```

**Facts:** Largest value strictly less than `target`. Time O(log n), space O(1).

---

## 5. `binary_serch_reverse_sorted_array.py`

### Code

```python
class Solution(object):
    def searchInReverseSorted(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < target:
                end = mid - 1
            else:
                start = mid + 1

        return False
```

### Flowchart

```mermaid
flowchart TD
    A[start=0, end=n-1] --> W{start <= end?}
    W -->|no| R[return False]
    W -->|yes| M[mid]
    M --> E{nums mid == target?}
    E -->|yes| T[return True]
    E -->|no| G{nums mid < target?}
    G -->|yes| L[end = mid - 1]
    G -->|no| H[start = mid + 1]
    L --> W
    H --> W
```

**Facts:** Descending order flips which half to take versus classic search. Time O(log n), space O(1).

---

## 6. `no_of_times_sorted_array_is_rotated.py`

### Code

```python
class Solution(object):
    def countArrayRotation(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] <= nums[right]:
                return left

            mid = left + (right - left) // 2

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid

        return left
```

### Flowchart

```mermaid
flowchart TD
    A[left=0, right=n-1] --> W{left < right?}
    W -->|no| R[return left]
    W -->|yes| S{nums left <= nums right?}
    S -->|yes| Z[return left no rotation slice]
    S -->|no| M[mid]
    M --> H{nums mid >= nums left?}
    H -->|yes| L[left = mid + 1]
    H -->|no| RR[right = mid]
    L --> W
    RR --> W
```

**Facts:** Index of minimum = rotation count (distinct ascending rotated). Time O(log n), space O(1).

---

## 7. `leetcode_153_find_minimum_in_rotated_sorted_array.py`

### Code

```python
class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
```

### Flowchart

```mermaid
flowchart TD
    A[l=0, r=n-1] --> W{l < r?}
    W -->|no| R[return nums l]
    W -->|yes| M[mid]
    M --> G{nums mid > nums r?}
    G -->|yes| L[l = mid + 1]
    G -->|no| RR[r = mid]
    L --> W
    RR --> W
```

**Facts:** Compare `mid` to **right** boundary; minimum lies in unsorted half. Time O(log n), space O(1).

---

## 8. `leetcode_744_find_letter_greater_than_target.py`

### Code

```python
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start = 0
        end = len(letters) - 1
        result = None

        while start <= end:
            mid = (start + end) // 2

            if letters[mid] == target:
                start = mid + 1
            elif letters[mid] > target:
                result = letters[mid]
                end = mid - 1
            else:
                start = mid + 1

        return result if result is not None else letters[0]
```

### Flowchart

```mermaid
flowchart TD
    A[result = None] --> W{start <= end?}
    W -->|no| C{result set?}
    C -->|yes| R1[return result]
    C -->|no| R2[return letters 0 wrap]
    W -->|yes| M[mid]
    M --> E{letters mid == target?}
    E -->|yes| S[start = mid + 1]
    E -->|no| G{letters mid > target?}
    G -->|yes| U[result = letters mid, end = mid - 1]
    G -->|no| V[start = mid + 1]
    S --> W
    U --> W
    V --> W
```

**Facts:** Smallest letter strictly greater than `target`; else first letter. Time O(log n), space O(1).

---

## 9. `leetcode_2529_max_count_of_positive_negative_integer.py`

### Code

```python
class Solution(object):
    def maximumCount(self, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        pos = len(nums) - left

        left = 0
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == 0:
                right = mid - 1
            else:
                left = mid + 1

        neg = left

        return pos if pos > neg else neg
```

### Flowchart — pass 1 (`pos`)

```mermaid
flowchart TD
    A[left=0, right=n-1] --> W{left <= right?}
    W -->|no| P[pos = n - left]
    W -->|yes| M[mid = left+right >> 1]
    M --> Q{nums mid > 0?}
    Q -->|yes| R[right = mid - 1]
    Q -->|no| L[left = mid + 1]
    R --> W
    L --> W
```

### Flowchart — pass 2 (`neg`, same `right` variable as when pass 1 ended)

```mermaid
flowchart TD
    A[left = 0] --> W{left <= right?}
    W -->|no| N[neg = left]
    W -->|yes| M[mid = left+right >> 1]
    M --> Z{nums mid == 0?}
    Z -->|yes| RR[right = mid - 1]
    Z -->|no| LL[left = mid + 1]
    RR --> W
    LL --> W
    N --> X{return max pos, neg}
```

**ASCII**

```
pos = number of strictly positive values = len(nums) - (first index i with nums[i] > 0).

neg = number of strictly negative values: second loop uses the file’s left/right state (right not reset to n-1).
```

**Facts:** Two binary searches; time O(log n), space O(1).

---

## More topics

- [ARRAYS_FLOWCHARTS.md](../arrays/ARRAYS_FLOWCHARTS.md)
- [RECURSION_FLOWCHARTS.md](../recursion_backtracking/RECURSION_FLOWCHARTS.md)
