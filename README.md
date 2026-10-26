# PDSA — Programming, Data Structures and Algorithms (Sep 2026)

Graded Programming Assignment (GRPA) and Practice Programming Assignment (PPA)
solutions for the **PDSA** course, structured as a clean Python package.

---

## Project Structure

```
PDSA_SEP_2026/
├── week1/
│   ├── __init__.py
│   ├── grpa1_min_difference.py               # Minimum difference among P elements
│   └── grpa2_goldbach.py                     # Goldbach's Conjecture
│
├── week2/
│   ├── __init__.py
│   ├── grpa1_combination_sort.py             # Stable letter + number sort
│   ├── grpa2_find_largest.py                 # Largest in sorted-rotated list (O(log n))
│   ├── grpa3_merge_in_place.py               # In-place merge (swap-only)
│   ├── ppa1_binary_search.py                 # Binary search with comparison count
│   └── ppa2_counting_sort.py                 # Counting sort for bounded range
│
├── week3/
│   ├── __init__.py
│   ├── grpa1_dish_prepare_order.py           # Frequency sort with tie-breaking
│   ├── grpa2_evaluate_expression.py          # Postfix (RPN) expression evaluator
│   ├── grpa3_reverse_linked_list.py          # Singly linked list reversal
│   └── ppa1_doubly_linked_list.py            # Doubly linked list (O(1) tail ops)
│
├── live_coding_problems/
│   ├── __init__.py
│   ├── week2_find_peak.py                    # Binary search for peak element
│   ├── week2_find_common_elements.py         # Sort + two-pointer common elements
│   ├── week2_merge_sort_subordinates.py      # Merge sort with people counter
│   ├── week2_find_pair_sum.py                # Sort + two-pointer pair sum
│   ├── week3_remove_duplicates.py            # Remove duplicates from sorted LL
│   ├── week3_doubly_ll_insert_at_pos.py      # Doubly LL insert_at_pos
│   ├── week3_merge_sorted_ll.py              # Merge two sorted linked lists
│   └── week3_stack_using_queues.py           # Stack implemented with two queues
│
├── concept_questions/
│   ├── __init__.py
│   └── week3_first_eligible_binary_search.py # First eligible student (binary search)
│
├── EXPLANATION.md
└── README.md
```

---

## Topics Covered

| Week | Topics |
|------|--------|
| **Week 1** | Sorting, Sliding Window, Number Theory (Primality) |
| **Week 2** | Stable Sort, Binary Search, In-Place Merge, Counting Sort |
| **Week 3** | Hash Maps, Stacks (RPN), Linked Lists (Singly & Doubly) |
| **Live — Week 2** | Binary search peak, two-pointer pair/common, merge sort counting |
| **Live — Week 3** | LL duplicate removal, doubly LL insertion, sorted LL merge, stack from queues |

---

## How to Run

```bash
# GRPA / PPA modules
python -m week1.grpa1_min_difference
python -m week2.ppa1_binary_search
python -m week3.grpa2_evaluate_expression
python -m week3.ppa1_doubly_linked_list

# Live coding problems (all read from stdin)
python live_coding_problems/week2_find_peak.py
python live_coding_problems/week2_find_common_elements.py
python live_coding_problems/week2_merge_sort_subordinates.py
python live_coding_problems/week2_find_pair_sum.py
python live_coding_problems/week3_remove_duplicates.py
python live_coding_problems/week3_doubly_ll_insert_at_pos.py
python live_coding_problems/week3_merge_sorted_ll.py
python live_coding_problems/week3_stack_using_queues.py
```

> **Python 3.10+** required.

---

## Code Standards (clean-python)

| Rule | Applied |
|------|---------|
| `PY1` | Type hints on all public functions |
| `G3`  | Named constants replace magic values |
| `F5`  | Guard clauses flatten deep nesting |
| `M8`  | Private helpers prefixed with `_` |
| `C1/C5` | No metadata or dead comments |

---

## License

Personal academic reference only — not for redistribution.
