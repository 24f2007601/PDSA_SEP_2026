# Program Explanations

Detailed walkthroughs for every GRPA and PPA solution in this repository.

---

## 1. `week1/grpa1_min_difference.py` — Minimum Difference among P Elements

### Problem

Given a list of integers and a positive integer `subset_size`, pick `subset_size` elements such that the difference between the maximum and minimum of the chosen elements is as small as possible. Return that minimum difference.

### Algorithm — Sort + Sliding Window

```
1.  Create a sorted copy of the numbers.
2.  Slide a window of `subset_size` across the sorted list.
3.  For each window, compute  sorted[i + subset_size - 1] - sorted[i].
4.  Track and return the smallest such difference.
```

### Why It Works

After sorting, any optimal subset must be **contiguous** in the sorted order (picking a non-contiguous subset would only widen the gap). So we just need the minimum range across all contiguous windows.

### Step-by-Step Example

```
numbers = [3, 4, 1, 9, 56, 7, 9, 12],  subset_size = 5

After sorting:  [1, 3, 4, 7, 9, 9, 12, 56]

Window 0 → [1, 3, 4, 7, 9]    →  9 - 1  = 8
Window 1 → [3, 4, 7, 9, 9]    →  9 - 3  = 6
Window 2 → [4, 7, 9, 9, 12]   → 12 - 4  = 8
Window 3 → [7, 9, 9, 12, 56]  → 56 - 7  = 49

Minimum difference = 6  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Sorting | O(n log n) |
| Sliding window | O(n) |
| **Total** | **O(n log n)** |

---

## 2. `week1/grpa2_goldbach.py` — Goldbach's Conjecture

### Problem

Given an even number `n > 2`, return all pairs `(a, b)` where `a ≤ b`, both `a` and `b` are prime, and `a + b = n`.

### Algorithm — Iterate + Primality Check

```
1.  For each candidate  a  from 2 to n // 2:
      compute  b = n - a
      if both a and b are prime  →  add (a, b) to results
2.  Return the list of pairs.
```

The helper `is_prime(num)` uses trial division up to `√num`.

### Why `a` Only Goes to `n // 2`

For any pair `(a, b)` with `a ≤ b`, we know `a ≤ n/2`. Iterating further would produce duplicate reversed pairs.

### Step-by-Step Example

```
n = 26

a =  2 → b = 24 → 24 not prime  ✗
a =  3 → b = 23 → both prime    ✔  → (3, 23)
a =  7 → b = 19 → both prime    ✔  → (7, 19)
a = 13 → b = 13 → both prime    ✔  → (13, 13)

Result = [(3, 23), (7, 19), (13, 13)]  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Outer loop | O(n) |
| `is_prime` per call | O(√n) |
| **Total** | **O(n √n)** |

---

## 3. `week2/grpa1_combination_sort.py` — Combination Sort

### Problem

Given a list of unique strings where each string starts with a letter (`a`–`z`) followed by a number (`0`–`99`), return two sorted lists:

- **by_letter** — sorted by the first character only (stable — same-character strings keep their original order).
- **by_letter_and_number** — sorted by first character ascending, then by number descending within each character group.

### Algorithm — Stable Sort with Custom Keys

```
1.  by_letter = sorted(str_list, key = first character only)
       Python's Timsort is stable, so same-character strings
       preserve their original relative order.

2.  by_letter_and_number = sorted(str_list, key = (first character, -number))
       Negating the number gives descending numeric order
       within each character group.
```

### Step-by-Step Example

```
Input: ['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']

by_letter (sort by letter, preserve original order within same letter):
  b: b87
  c: c65
  d: d34, d12, d77   ← original order kept
  g: g54, g1, g40, g5
→ ['b87', 'c65', 'd34', 'd12', 'd77', 'g54', 'g1', 'g40', 'g5']  ✔

by_letter_and_number (sort by letter, then number descending):
  d: d77, d34, d12   ← 77 > 34 > 12
  g: g54, g40, g5, g1
→ ['b87', 'c65', 'd77', 'd34', 'd12', 'g54', 'g40', 'g5', 'g1']  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Each `sorted()` call | O(n log n) |
| **Total** | **O(n log n)** |

---

## 4. `week2/grpa2_find_largest.py` — Largest in a Sorted & Rotated List

### Problem

A sorted (ascending) list of unique numbers has been rotated an unknown number of times. Find the largest element in **O(log n)** time using binary search (no list slicing).

### Algorithm — Modified Binary Search

```
1.  If the list is not rotated (numbers[0] ≤ numbers[-1]), return the last element.
2.  Otherwise, binary search for the pivot:
      a.  Compute mid.
      b.  If numbers[mid] > numbers[mid + 1]  →  numbers[mid] is the peak.
      c.  If numbers[mid] < numbers[mid - 1]  →  numbers[mid - 1] is the peak.
      d.  If numbers[mid] ≥ numbers[low]      →  left half is sorted, search right.
      e.  Else                                 →  search left.
```

### Why It Works

In a rotated sorted array, there is exactly **one pivot** where the value drops. The largest element is immediately before this drop. Comparing `numbers[mid]` with `numbers[low]` determines which half contains the pivot.

### Step-by-Step Example

```
numbers = [7, 8, 2, 4, 5]

low = 0, high = 4
numbers[0] = 7 > numbers[4] = 5  →  list IS rotated

Iteration 1:
  mid = 2,  numbers[2] = 2
  numbers[2] < numbers[1] (2 < 8)  →  peak is numbers[1] = 8

Return 8  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Binary search | O(log n) |
| **Total** | **O(log n)** |

---

## 5. `week2/grpa3_merge_in_place.py` — Merge Two Sorted Arrays In Place

### Problem

Given two `SwappableList` objects `a` and `b` (sorted ascending), merge them **in place** so that `a` holds the smallest `len(a)` elements and `b` the rest — both still sorted. The only mutation allowed is the `.swap()` method.

### Algorithm — Compare-and-Swap with Insertion Sort on B

```
1.  For each index i in a:
      if a[i] > b[0]:
        a.  Swap a[i] with b[0].
        b.  Bubble b[0] to its correct position in b
            (repeated adjacent swaps until b is sorted again).
```

### Why It Works

Iterating through `a` left-to-right, whenever an element in `a` is larger than the smallest in `b`, they are in the wrong container — so we swap. A single bubble pass restores order in `b` because only one element is displaced.

### Step-by-Step Example

```
a = [2, 4, 6, 9, 13, 15]
b = [1, 3, 5, 10]

i=0: a[0]=2 > b[0]=1 → swap → a=[1,4,6,9,13,15]  b=[2,3,5,10]
i=1: a[1]=4 > b[0]=2 → swap → a=[1,2,6,9,13,15]  b=[4,3,5,10] → bubble → [3,4,5,10]
i=2: a[2]=6 > b[0]=3 → swap → a=[1,2,3,9,13,15]  b=[6,4,5,10] → bubble → [4,5,6,10]
i=3: a[3]=9 > b[0]=4 → swap → a=[1,2,3,4,13,15]  b=[9,5,6,10] → bubble → [5,6,9,10]
i=4: a[4]=13 > b[0]=5 → swap → a=[1,2,3,4,5,15]  b=[13,6,9,10] → bubble → [6,9,10,13]
i=5: a[5]=15 > b[0]=6 → swap → a=[1,2,3,4,5,6]   b=[15,9,10,13] → bubble → [9,10,13,15]

Final:  a = [1, 2, 3, 4, 5, 6]   b = [9, 10, 13, 15]  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Outer loop over a | O(n) |
| Bubble pass in b per swap | O(m) |
| **Total (worst case)** | **O(n × m)** |

---

## 6. `week2/ppa1_binary_search.py` — Binary Search with Comparison Count

### Problem

Given a sorted list and a target integer, perform binary search and return `(found, num_comparisons)`.

### Algorithm — Standard Binary Search with Counter

```
1.  Set left = 0, right = len - 1, num_comparisons = 0.
2.  While left ≤ right:
      a.  mid = (left + right) // 2
      b.  num_comparisons += 1
      c.  If sorted_list[mid] == target  →  return (True, num_comparisons)
      d.  If sorted_list[mid] < target   →  left = mid + 1
      e.  Else                           →  right = mid - 1
3.  Return (False, num_comparisons).
```

### Step-by-Step Example

```
sorted_list = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65],  target = 11

Iteration 1:  left=0, right=10, mid=5  → 23 > 11 → right=4   (comparisons=1)
Iteration 2:  left=0, right=4,  mid=2  →  8 < 11 → left=3    (comparisons=2)
Iteration 3:  left=3, right=4,  mid=3  → 11 == 11 → FOUND    (comparisons=3)

Return (True, 3)  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Binary search | O(log n) |
| **Total** | **O(log n)** |

---

## 7. `week2/ppa2_counting_sort.py` — Counting Sort for Bounded Range

### Problem

Given a list of `n` integers where each value is in `[0, upper_bound)`, sort the list **in place** in O(n + r) time.

### Algorithm — Counting Sort

```
1.  Create a counts array of size upper_bound, initialized to 0.
2.  For each number in the list, increment  counts[number].
3.  Overwrite the list in place:
      For each value 0 to upper_bound - 1:
        write that value  counts[value]  times.
```

### Why It Works

Since every element falls in a known, small range `[0, upper_bound)`, we count occurrences (O(n)), then reconstruct the sorted list by writing each value the correct number of times (O(n + r)). No comparison-based sorting is needed.

### Step-by-Step Example

```
numbers = [2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2],  upper_bound = 4

Count:   counts = [3, 4, 5, 2]   (three 0s, four 1s, five 2s, two 3s)

Overwrite:
  val=0: write 0 ×3  → [0, 0, 0, ...]
  val=1: write 1 ×4  → [0, 0, 0, 1, 1, 1, 1, ...]
  val=2: write 2 ×5  → [..., 2, 2, 2, 2, 2, ...]
  val=3: write 3 ×2  → [..., 3, 3]

Result = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3]  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Counting | O(n) |
| Reconstructing | O(n + r) |
| **Total** | **O(n + r)** |
