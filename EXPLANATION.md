# Program Explanations

Detailed walkthroughs for every GRPA solution in this repository.

---

## 1. `grpa1_w1.py` — Minimum Difference among P Elements

### Problem

Given a list `L` of integers and a positive integer `P`, pick `P` elements from `L` such that the difference between the maximum and minimum of the chosen elements is as small as possible. Return that minimum difference.

### Algorithm — Sort + Sliding Window

```
1.  Sort L in ascending order.
2.  Slide a window of size P across the sorted list.
3.  For each window, compute  L[i + P - 1] - L[i].
4.  Track and return the smallest such difference.
```

### Why It Works

After sorting, any optimal subset of `P` elements must be **contiguous** in the sorted order (picking a non-contiguous subset would only widen the gap). So we just need the minimum range across all contiguous windows of size `P`.

### Step-by-Step Example

```
L = [3, 4, 1, 9, 56, 7, 9, 12],  P = 5

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

## 2. `grpa 2_w1.py` — Goldbach's Conjecture

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
a =  4 → b = 22 → 4 not prime   ✗
a =  5 → b = 21 → 21 not prime  ✗
a =  6 → b = 20 → 6 not prime   ✗
a =  7 → b = 19 → both prime    ✔  → (7, 19)
a =  8 → b = 18 → 8 not prime   ✗
a =  9 → b = 17 → 9 not prime   ✗
a = 10 → b = 16 → 10 not prime  ✗
a = 11 → b = 15 → 15 not prime  ✗
a = 12 → b = 14 → 12 not prime  ✗
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

## 3. `grpa2_w2.py` — Largest Element in a Sorted & Rotated List

### Problem

A sorted (ascending) list of unique numbers has been rotated an unknown number of times. Find the largest element in **O(log n)** time using binary search (no list slicing).

### Algorithm — Modified Binary Search

```
1.  If the list is not rotated (L[0] ≤ L[-1]), the largest is the last element.
2.  Otherwise, use binary search:
      a.  Compute mid.
      b.  If L[mid] > L[mid + 1]  →  L[mid] is the peak.
      c.  If L[mid] < L[mid - 1]  →  L[mid - 1] is the peak.
      d.  If L[mid] ≥ L[low]      →  left half is sorted, search right.
      e.  Else                     →  right half is sorted, search left.
```

### Why It Works

In a rotated sorted array, there is exactly **one "pivot"** point where the value drops. The largest element is immediately before this drop. By comparing `L[mid]` with `L[low]`, we determine which half is properly sorted and narrow the search toward the unsorted half (which contains the pivot).

### Step-by-Step Example

```
L = [7, 8, 2, 4, 5]

low = 0, high = 4
L[0] = 7 > L[4] = 5  →  list IS rotated

Iteration 1:
  mid = 2,  L[2] = 2
  L[2] < L[1] (2 < 8)  →  peak is L[1] = 8

Return 8  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Binary search | O(log n) |
| **Total** | **O(log n)** |

---

## 4. `grpa3_w2.py` — Merge Two Sorted Arrays In Place

### Problem

Given two `MyList` objects `A` and `B` (sorted ascending), merge them **in place** so that `A` holds the smallest `len(A)` elements and `B` holds the rest — both still sorted. The only mutation allowed is the `swap` method.

### Algorithm — Compare-and-Swap with Insertion Sort on B

```
1.  For each index i in A:
      if A[i] > B[0]:
        a.  Swap A[i] with B[0].
        b.  "Bubble" B[0] to its correct position in B
            (repeated adjacent swaps until B is sorted again).
```

### Why It Works

We iterate through `A` left-to-right. Whenever an element in `A` is larger than the smallest element in `B`, they are in the wrong container — so we swap them. After the swap, `B` may be unsorted, but a single insertion-sort pass (bubbling the new `B[0]` rightward) restores order in `B` because only one element is out of place.

### Step-by-Step Example

```
A = [2, 4, 6, 9, 13, 15]
B = [1, 3, 5, 10]

i=0: A[0]=2 > B[0]=1 → swap → A=[1,4,6,9,13,15]  B=[2,3,5,10]
i=1: A[1]=4 > B[0]=2 → swap → A=[1,2,6,9,13,15]  B=[4,3,5,10] → bubble B → [3,4,5,10]
i=2: A[2]=6 > B[0]=3 → swap → A=[1,2,3,9,13,15]  B=[6,4,5,10] → bubble B → [4,5,6,10]
i=3: A[3]=9 > B[0]=4 → swap → A=[1,2,3,4,13,15]  B=[9,5,6,10] → bubble B → [5,6,9,10]
i=4: A[4]=13 > B[0]=5 → swap → A=[1,2,3,4,5,15]  B=[13,6,9,10] → bubble B → [6,9,10,13]
i=5: A[5]=15 > B[0]=6 → swap → A=[1,2,3,4,5,6]   B=[15,9,10,13] → bubble B → [9,10,13,15]

Final:  A = [1, 2, 3, 4, 5, 6]   B = [9, 10, 13, 15]  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Outer loop over A | O(n) |
| Bubble pass in B per swap | O(m) |
| **Total (worst case)** | **O(n × m)** |

Where `n = len(A)` and `m = len(B)`.
