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

---

## 8. `week3/grpa1_dish_prepare_order.py` — Dish Preparation Order

### Problem

A restaurant receives `n` orders as a list of dish IDs. Return the unique dish IDs in **descending order of frequency** (most-ordered first). Break ties by **ascending dish ID**.

### Algorithm — Frequency Map + Compound Sort Key

```
1.  Build a frequency map:  dish_id → count.
2.  Sort the map's items by key = (-count, dish_id).
3.  Return the sorted dish IDs.
```

### Why `-count` for Descending Order

Python's `sorted()` is ascending by default. Negating `count` turns the largest count into the smallest key, achieving descending frequency with a single sort pass.

### Step-by-Step Example

```
order_list = [1004,1003,1004,1003,1004,1005,1003,1004,1003,1002,1005,1002,1002,1001,1002,1002,1002]

Frequency map:
  1001 → 1
  1002 → 6
  1003 → 4
  1004 → 4
  1005 → 2

Sort by (-freq, id):
  (-6, 1002) → 1002
  (-4, 1003) → 1003
  (-4, 1004) → 1004   ← same freq, smaller ID first
  (-2, 1005) → 1005
  (-1, 1001) → 1001

Result = [1002, 1003, 1004, 1005, 1001]  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Building frequency map | O(n) |
| Sorting k unique dishes | O(k log k) |
| **Total** | **O(n + k log k)** |

---

## 9. `week3/grpa2_evaluate_expression.py` — Postfix Expression Evaluator

### Problem

Evaluate a postfix (Reverse Polish Notation) expression string where tokens are separated by spaces. Supported operators: `+`, `-`, `*`, `/`, `**`.

### Algorithm — Stack-Based Evaluation

```
1.  Split the expression into tokens.
2.  For each token:
      • If it's a number  →  push float(token) onto the stack.
      • If it's an operator  →  pop B then pop A, compute A op B, push result.
3.  The single remaining stack value is the answer.
```

### Why Pop Order Matters

The **first** pop is the **right** operand (B) and the **second** pop is the **left** operand (A). For non-commutative operators (`-`, `/`, `**`) this order is critical.

### Step-by-Step Example

```
Expression: "2 3 1 * + 9 -"

Token  2 → stack: [2.0]
Token  3 → stack: [2.0, 3.0]
Token  1 → stack: [2.0, 3.0, 1.0]
Token  * → pop 1.0(B), 3.0(A) → 3.0 * 1.0 = 3.0  →  stack: [2.0, 3.0]
Token  + → pop 3.0(B), 2.0(A) → 2.0 + 3.0 = 5.0  →  stack: [5.0]
Token  9 → stack: [5.0, 9.0]
Token  - → pop 9.0(B), 5.0(A) → 5.0 - 9.0 = -4.0 →  stack: [-4.0]

Result = -4.0  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Tokenising & scanning | O(n) |
| Each push / pop | O(1) |
| **Total** | **O(n)** |

---

## 10. `week3/grpa3_reverse_linked_list.py` — Reverse a Singly Linked List

### Problem

Given the head node of a singly linked list, reverse the list **in place** by rewiring `next` pointers only. No new nodes may be created and no values may be swapped.

### Algorithm — Three-Pointer Iteration

```
prev    = None
current = root

While current is not None:
    next_node   = current.next   ← save successor
    current.next = prev          ← reverse the pointer
    prev        = current        ← advance prev
    current     = next_node      ← advance current

Return prev   ← new head
```

### Why Three Pointers

- `prev` tracks the already-reversed portion (new chain growing leftward).
- `current` is the node being processed.
- `next_node` preserves the original successor before it is overwritten.

### Step-by-Step Example

```
Original: 64 → 7 → 28 → 43 → 3 → None

Step 1:  prev=None,  current=64  → 64.next=None,  prev=64,  current=7
Step 2:  prev=64,    current=7   → 7.next=64,     prev=7,   current=28
Step 3:  prev=7,     current=28  → 28.next=7,     prev=28,  current=43
Step 4:  prev=28,    current=43  → 43.next=28,    prev=43,  current=3
Step 5:  prev=43,    current=3   → 3.next=43,     prev=3,   current=None

Return 3  →  3 → 43 → 28 → 7 → 64 → None  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Single pass through list | O(n) |
| **Total** | **O(n)** |
| **Space** | **O(1)** |

---

## 11. `week3/ppa1_doubly_linked_list.py` — Doubly Linked List (O(1) Tail Operations)

### Problem

Implement a doubly linked list with two O(1) methods:
- `insert_end(data)` — append to the tail.
- `delete_end()` — remove from the tail.

### Data Structure

Each `Node` stores `data`, `next` (→ successor), and `prev` (→ predecessor).  
The list maintains `head` (first node) and `last` (last node) pointers to avoid traversal.

### Algorithm — `insert_end`

```
1.  Create new_node.
2.  If list is empty  →  head = last = new_node.
3.  Else:
      new_node.prev = last
      last.next     = new_node
      last          = new_node
```

### Algorithm — `delete_end`

```
1.  If list is empty → return.
2.  If only one node → head = last = None.
3.  Else:
      last      = last.prev
      last.next = None
```

Both operations touch only the `last` pointer and its immediate neighbour — no traversal needed, so both run in **O(1)**.

### Step-by-Step Example

```
Insert 1, 3, 5, 7, 9:
  head=1 ↔ 3 ↔ 5 ↔ 7 ↔ 9=last

delete_end():  removes 9  →  head=1 ↔ 3 ↔ 5 ↔ 7=last
delete_end():  removes 7  →  head=1 ↔ 3 ↔ 5=last

Forward  (head → last):  1,3,5  ✔
Backward (last → head):  5,3,1  ✔
```

### Time Complexity

| Operation | Cost |
|-----------|------|
| `insert_end` | O(1) |
| `delete_end` | O(1) |
| `__str__` (traversal) | O(n) |

---

## 12. `concept_questions/concept3.py` — First Eligible Student (Binary Search on Sorted Binary List)

### Problem

A sorted list contains only `0`s ("not eligible") and `1`s ("eligible"), with all `0`s appearing before all `1`s. Find the **zero-based index of the first `1`**. Return `-1` if no `1` exists.

### Why Binary Search?

A linear scan would work in O(n), but since the list is **sorted**, we can exploit the structure and halve the search space each step — achieving **O(log n)**.

### Algorithm — Left-Boundary Binary Search

```
1.  Set left = 0, right = len - 1, first_eligible = -1.
2.  While left ≤ right:
      a.  mid = (left + right) // 2
      b.  If status[mid] == 1:
            record first_eligible = mid
            search LEFT  →  right = mid - 1   (might be an earlier 1)
      c.  Else (status[mid] == 0):
            search RIGHT →  left  = mid + 1   (first 1 must be here or later)
3.  Return first_eligible.
```

### Key Insight

When `status[mid] == 1`, **do not stop** — save the index as a candidate and keep searching left. The first `1` could still be at a smaller index. Only stop when `left > right`.

### Step-by-Step Example

```
status = [0, 0, 0, 1, 1, 1]
          0  1  2  3  4  5

left=0, right=5
─────────────────────────────────────────────────────
Iter 1:  mid = 2  →  status[2] = 0  →  left  = 3
Iter 2:  mid = 4  →  status[4] = 1  →  first_eligible = 4,  right = 3
Iter 3:  mid = 3  →  status[3] = 1  →  first_eligible = 3,  right = 2
Iter 4:  left(3) > right(2)  →  stop

Return 3  ✔
```

### Edge Cases

| Input | Behaviour | Output |
|-------|-----------|--------|
| `[1, 1, 1, 1, 1, 1]` | First `mid` is 1; keeps going left until boundary | `0` |
| `[0, 0, 0, 0, 0]` | Never records a candidate | `-1` |
| `[0, 0, 1, 1, 1]` | Finds first 1 at index 2 | `2` |
| `[1]` | Single-element 1, found immediately | `0` |
| `[0]` | Single-element 0, never recorded | `-1` |

### Time Complexity

| Step | Cost |
|------|------|
| Binary search | O(log n) |
| **Total** | **O(log n)** |
| **Space** | **O(1)** |

---

## 13. `live_coding_problems/week3_p1.py` — Remove Duplicates from Sorted Linked List

### Problem

Given a non-empty singly linked list with `n` nodes sorted in **ascending order**, remove all nodes with duplicate values so that each value appears only once. The function `removeDuplicate(head)` must modify the list **in place** and return nothing.

### Algorithm — Single-Pass Pointer Walk

```
current = head
While current and current.next exist:
    If current.data == current.next.data:
        current.next = current.next.next   ← skip the duplicate
    Else:
        current = current.next             ← advance
```

### Why It Works

Because the list is **sorted**, all duplicates are **adjacent**. A single left-to-right pass is sufficient — whenever the next node matches the current one, bypass it by rewiring `current.next`. No second pass is ever needed.

### Step-by-Step Example

```
Input:  1 → 1 → 2 → 2 → 2 → 3 → 3 → 4 → 4 → 4 → 4 → 5 → 7 → 9

current=1: next=1, same  → skip → 1 → 2 → 2 → 2 → 3 ...
current=1: next=2, diff  → advance
current=2: next=2, same  → skip
current=2: next=2, same  → skip
current=2: next=3, diff  → advance
... (continues)

Output: Output Linked List: 1 2 3 4 5 7 9  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Single pass | O(n) |
| **Total** | **O(n)** |
| **Space** | **O(1)** |

---

## 14. `live_coding_problems/week3_p2.py` — Doubly Linked List: `insert_at_pos`

### Problem

Given the class `doubly_linked_list` (with `head` and `last` pointers) and `Node` (with `data`, `next`, `prev`), implement:

`insert_at_pos(data, pos)` — insert a new node at position `pos`, where `1 < pos <= length(list)`.

### Algorithm — Traverse to (pos − 1), Rewire

```
1. Create new_node with given data.
2. Walk from head to node at position (pos - 1) → call it `current`.
3. Let next_node = current.next.
4. Wire up:
     new_node.prev = current
     new_node.next = next_node
     current.next  = new_node
     if next_node exists: next_node.prev = new_node
     else: self.last = new_node   (inserted at tail)
```

### Step-by-Step Example

```
List:   1 ↔ 3 ↔ 5 ↔ 7 ↔ 9,   insert 20 at pos=2

Traverse to pos-1=1  →  current = node(1)
next_node = node(3)

new_node(20).prev = node(1)
new_node(20).next = node(3)
node(1).next      = node(20)
node(3).prev      = node(20)

Result: 1 ↔ 20 ↔ 3 ↔ 5 ↔ 7 ↔ 9  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Traversal to pos | O(pos) |
| Pointer rewiring | O(1) |
| **Total (worst case)** | **O(n)** |

---

## 15. `live_coding_problems/week3_p3.py` — Merge Two Sorted Linked Lists

### Problem

Given two non-empty singly linked lists sorted in ascending order, merge them into one sorted linked list. `mergeSortedList(head1, head2)` must **return** the head of the merged list.

### Algorithm — Recursive Merge

```
Base cases:
    If head1 is None → return head2
    If head2 is None → return head1

If head1.data <= head2.data:
    head1.next = mergeSortedList(head1.next, head2)
    return head1
Else:
    head2.next = mergeSortedList(head1, head2.next)
    return head2
```

### Why It Works

At each step, we pick the smaller of the two current heads and recursively attach the rest of the merged list to it. The recursion unwinds naturally once either list is exhausted.

### Step-by-Step Example

```
L1: 1 → 3 → 5 → 7 → 9 → 11
L2: 2 → 4 → 6

merge(1, 2): 1 <= 2 → 1.next = merge(3, 2)
  merge(3, 2): 3 > 2  → 2.next = merge(3, 4)
    merge(3, 4): 3 <= 4 → 3.next = merge(5, 4)
      merge(5, 4): 5 > 4  → 4.next = merge(5, 6)
        merge(5, 6): 5 <= 6 → 5.next = merge(7, 6)
          merge(7, 6): 7 > 6  → 6.next = merge(7, None) = 7→9→11
        → 5 → 7 → 9 → 11
      → 4 → 5 → 7 → 9 → 11
    → 3 → 4 → 5 → 7 → 9 → 11
  → 2 → 3 → 4 → 5 → 7 → 9 → 11
→ 1 → 2 → 3 → 4 → 5 → 7 → 9 → 11

Output Linked List: 1 2 3 4 5 6 7 9 11  ✔
```

### Time Complexity

| Step | Cost |
|------|------|
| Recursive calls | O(n + m) |
| **Total** | **O(n + m)** |
| **Space (call stack)** | **O(n + m)** |
