# Solution Approach Diagrams

Visual representations of how each problem was solved. These diagrams render on **GitHub** when viewing this file.

---

## Sliding Window

### 643. Maximum Average Subarray I

**Concept:** Slide a fixed-size window and track max sum (avoid recomputing entire window each time).

```mermaid
flowchart LR
    subgraph "Initial Window (k=4)"
        W1["[1, 12, -5, -6]"]
        S1["sum = 2"]
    end

    subgraph "Slide Right"
        W2["[12, -5, -6, 50]"]
        S2["sum = 51 = prev - 1 + 50"]
    end

    W1 -->|"subtract 1, add 50"| W2
```

```mermaid
flowchart TD
    A[Compute sum of first k elements] --> B[Track as max_sum]
    B --> C[i = k to n-1]
    C --> D["window_sum += nums[i] - nums[i-k]"]
    D --> E{window_sum > max_sum?}
    E -->|Yes| F[max_sum = window_sum]
    E -->|No| G[Continue]
    F --> G
    G --> H{More elements?}
    H -->|Yes| C
    H -->|No| I[Return max_sum / k]
```

---

### Maximum Sum Subarray of Size K

```mermaid
flowchart LR
    subgraph " nums = [2, 1, 5, 1, 3, 2], k = 3 "
        A["Window 1: 2+1+5=8"]
        B["Window 2: 1+5+1=7"]
        C["Window 3: 5+1+3=9 ✓ max"]
        D["Window 4: 1+3+2=6"]
    end
    A --> B --> C --> D
```

---

## Binary Search

### 704. Binary Search (Classic)

```mermaid
flowchart TD
    A[start=0, end=n-1] --> B{start <= end?}
    B -->|No| C[Return -1]
    B -->|Yes| D[mid = start+end / 2]
    D --> E{nums[mid] == target?}
    E -->|Yes| F[Return mid]
    E -->|No| G{nums[mid] > target?}
    G -->|Yes| H[end = mid - 1]
    G -->|No| I[start = mid + 1]
    H --> B
    I --> B
```

---

### 153. Find Minimum in Rotated Sorted Array

```mermaid
flowchart LR
    subgraph "Rotated Array"
        A["[3, 4, 5 | 1, 2]"]
    end
    
    subgraph "Binary Search Logic"
        B["nums[mid] > nums[r]?"]
        B -->|Yes: min on right| C["l = mid + 1"]
        B -->|No: min at mid or left| D["r = mid"]
    end
```

---

## Hash Map

### 1. Two Sum (Hash Map Approach)

```mermaid
flowchart TD
    A[For each num at index i] --> B["complement = target - num"]
    B --> C{complement in seen?}
    C -->|Yes| D["Return [seen[complement], i]"]
    C -->|No| E["seen[num] = i"]
    E --> F[Next element]
    F --> A
```

**Example:** `nums = [2, 7, 11, 15], target = 9`
- i=0: num=2, complement=7, not in seen → `{2: 0}`
- i=1: num=7, complement=2, **in seen** → return `[0, 1]`

---

## Stack (Monotonic)

### Next Greater Element / Daily Temperatures

```mermaid
flowchart TD
    A[Traverse Right to Left] --> B{Stack empty?}
    B -->|Yes| C[result = -1]
    B -->|No| D{Stack top > current?}
    D -->|Yes| E[result = stack top]
    D -->|No| F[Pop until greater or empty]
    F --> B
    C --> G[Push current to stack]
    E --> G
```

```mermaid
flowchart LR
    subgraph "temperatures = [73, 74, 75, 71, 69, 72, 76]"
        T1["73"] --> T2["74"] --> T3["75"] --> T4["71"] --> T5["69"] --> T6["72"] --> T7["76"]
    end
    
    subgraph "Stack (right→left)"
        S["Pop smaller, next warmer = top"]
    end
```

---

## Two Pointers / Cycle Detection

### 141. Linked List Cycle (Floyd's Algorithm)

```mermaid
flowchart TD
    A[slow = head, fast = head] --> B{fast and fast.next exist?}
    B -->|No| C[Return False - no cycle]
    B -->|Yes| D["slow = slow.next, fast = fast.next.next"]
    D --> E{slow == fast?}
    E -->|Yes| F[Return True - cycle found]
    E -->|No| B
```

```mermaid
flowchart LR
    subgraph "Cycle"
        A((1)) --> B((2)) --> C((3)) --> D((4)) --> B
    end
    
    subgraph "Fast & Slow"
        S["slow: 1 step"]
        F["fast: 2 steps"]
        M["Eventually meet inside cycle"]
    end
```

---

## Heap

### 347. Top K Frequent Elements

```mermaid
flowchart TD
    A[Count frequency of each element] --> B[Build min-heap of size k]
    B --> C["Key: (-count, value) for max-heap behavior"]
    C --> D[For each num: push then pop if size > k]
    D --> E[Return elements in heap]
```

---

## Recursion / Backtracking

### 78. Subsets

```mermaid
flowchart TD
    A["dfs(idx, path)"] --> B{idx == n?}
    B -->|Yes| C[Add path to result]
    B -->|No| D[Exclude: dfs(idx+1, path)]
    D --> E[Include: dfs(idx+1, path + nums[idx])]
```

---

### 46. Permutations

```mermaid
flowchart TD
    A["backtrack(path)"] --> B{len path == n?}
    B -->|Yes| C[Add path to result]
    B -->|No| D[For each unused num]
    D --> E[Add num to path, mark used]
    E --> F[backtrack(path)]
    F --> G[Remove num, unmark]
    G --> D
```

---

## Legend

| Symbol | Meaning |
|--------|---------|
| `→` / `-->` | Flow / transition |
| `{ }` | Decision / condition |
| `[ ]` | Process / step |

---

*Diagrams use [Mermaid](https://mermaid.js.org/) syntax and render automatically on GitHub.*
