# Lecture 5: NumPy — Fundamentals, Array Operations & Broadcasting

---

## 1. NumPy Arrays vs. Python Sequences 💡 *(Interview Topic)*

While Python lists are dynamic referential arrays storing memory pointers to heterogeneous objects, NumPy arrays (`ndarray`) are contiguous blocks of homogeneous memory, engineered for high-performance numerical computing.

| Feature | Python Lists | NumPy `ndarray` |
| :--- | :--- | :--- |
| **Data Homogeneity** | Heterogeneous (mixed data types allowed) | Homogeneous (single contiguous data type) |
| **Memory Allocation** | Array of pointers to heap objects | Continuous, contiguous memory blocks |
| **Performance / Time** | Slower (requires pointer dereferencing) | Extremely Fast (vectorized C-level speed) |
| **Convenience** | Requires manual loops for element-wise ops | Supports direct vector mathematical operations |

### Axis Convention
When operating on multidimensional NumPy arrays:
* **`axis=0`:** Operates **vertically across rows** (down columns).
* **`axis=1`:** Operates **horizontally across columns** (across rows).

---

## 2. Array Creation Routines & Essential Syntax

```python
import numpy as np

# 1. Direct Creation
arr = np.array([1, 2, 3])

# 2. Range Creation: np.arange(start, stop, step)
range_arr = np.arange(1, 10, 2)  # Output: [1, 3, 5, 7, 9]

# 3. Constant Initializations
ones_matrix = np.ones((2, 3))    # 2x3 matrix filled with 1.0
zeros_matrix = np.zeros((3, 3))   # 3x3 matrix filled with 0.0

# 4. Linearly Spaced Elements: np.linspace(start, stop, num_points)
lin_arr = np.linspace(0, 1, 5)   # Output: [0.0, 0.25, 0.5, 0.75, 1.0]

# 5. Identity Matrix
identity_mat = np.identity(3)    # 3x3 diagonal identity matrix

# 6. Reshaping Arrays
reshaped_arr = np.arange(6).reshape((2, 3))
```

---

## 3. Essential Array Attributes

To inspect the structural mechanics of a NumPy array:

```python
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

print(a.ndim)     # Output: 2 (Number of dimensions/axes)
print(a.shape)    # Output: (2, 3) (Tuple specifying dimension lengths)
print(a.size)     # Output: 6 (Total number of elements in array)
print(a.itemsize) # Output: 4 (Space occupied by each element in bytes)
print(a.dtype)    # Output: int32 (Data type of elements)
```

---

## 4. Array Stacking, Splitting & Structural Manipulation

```python
x = np.array([1, 2])
y = np.array([3, 4])

# Stacking
v_stacked = np.vstack((x, y))  # Stacks vertically -> [[1, 2], [3, 4]]
h_stacked = np.hstack((x, y))  # Stacks horizontally -> [1, 2, 3, 4]

# Splitting
arr = np.arange(6)
split_arr = np.split(arr, 3)   # Splits array into 3 equal sub-arrays
```

---

## 5. Built-in Utility & Manipulation Functions

### Basic Operations (`sort`, `append`, `concatenate`, `unique`, `expand_dims`)
```python
a = np.array([4, 2, 1, 3])

# Sorting & Appending
sorted_a = np.sort(a)                          # Returns sorted array [1, 2, 3, 4]
appended_a = np.append(a, [5, 6])              # Appends elements at the end
concat_a = np.concatenate((a, np.array([9])))  # Merges arrays

# Unique Elements
u_vals = np.unique(np.array([1, 1, 2, 3]))    # Returns [1, 2, 3]

# Expanding Dimensions
arr = np.array([1, 2, 3])                      # Shape (3,)
expanded = np.expand_dims(arr, axis=0)         # Shape becomes (1, 3)
```

### Conditionals, Searching & Index Extraction
```python
arr = np.array([10, 20, 30, 40, 50])

# np.where(condition, [x, y]): Conditional replacement or index retrieval
idx = np.where(arr > 25)                       # Returns indices where condition is True -> (array([2, 3, 4]),)
replaced = np.where(arr > 25, 1, 0)            # Output: [0, 0, 1, 1, 1]

# Index Extractor Functions
max_idx = np.argmax(arr)                       # Returns index of maximum value -> 4
min_idx = np.argmin(arr)                       # Returns index of minimum value -> 0

# Cumulative Aggregations
cum_sum = np.cumsum(arr)                       # Output: [10, 30, 60, 100, 150]
cum_prod = np.cumprod(np.array([1, 2, 3, 4]))  # Output: [1, 2, 6, 24]

# Multiple Item Search: np.isin
mask = np.isin(arr, [20, 50, 90])              # Output: [False, True, False, False, True]
```

### Mutation & Clipping (`put`, `delete`, `clip`)
```python
a = np.array([10, 20, 30, 40, 50])

# np.put: Mutates array in-place at specified flat indices
np.put(a, [0, 2], [99, 88])                    # Array is now [99, 20, 88, 40, 50]

# np.delete: Removes elements at specified indices
deleted = np.delete(a, [1])                    # Returns [99, 88, 40, 50]

# np.clip: Restricts values within a [min, max] range
data = np.array([1, 5, 12, 20, 25])
clipped = np.clip(data, a_min=5, a_max=20)    # Output: [5, 5, 12, 20, 20]
```

---

## 6. Set Operations

NumPy provides built-in 1D set functions for mathematical set comparisons:

```python
s1 = np.array([1, 2, 3, 4])
s2 = np.array([3, 4, 5, 6])

union = np.union1d(s1, s2)        # Output: [1, 2, 3, 4, 5, 6]
intersection = np.intersect1d(s1, s2) # Output: [3, 4]
diff = np.setdiff1d(s1, s2)       # Elements in s1 but not in s2 -> [1, 2]
xor = np.setxor1d(s1, s2)         # Elements in s1 or s2, but not both -> [1, 2, 5, 6]
in_set = np.in1d(s1, [2, 4])      # Check presence -> [False, True, False, True]
