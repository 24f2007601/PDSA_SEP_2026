# PDSA — Programming, Data Structures and Algorithms (Sep 2026)

Graded Programming Assignment (GRPA) and Practice Programming Assignment (PPA) solutions for the **PDSA** course.

## Project Structure

```
PDSA_SEP_2026/
├── week1/
│   ├── __init__.py
│   ├── grpa1_min_difference.py      # Minimum difference among P elements
│   └── grpa2_goldbach.py            # Goldbach's Conjecture
├── week2/
│   ├── __init__.py
│   ├── grpa1_combination_sort.py    # Stable letter + number sort
│   ├── grpa2_find_largest.py        # Largest in sorted-rotated list
│   ├── grpa3_merge_in_place.py      # In-place merge (swap-only)
│   ├── ppa1_binary_search.py        # Binary search with comparison count
│   └── ppa2_counting_sort.py        # Counting sort for bounded range
├── week3/
│   ├── __init__.py
│   ├── grpa1_dish_prepare_order.py  # Frequency sort with tie-breaking
│   ├── grpa2_evaluate_expression.py # Postfix (RPN) expression evaluator
│   ├── grpa3_reverse_linked_list.py # Singly linked list reversal
│   └── ppa1_doubly_linked_list.py   # Doubly linked list (O(1) tail ops)
├── live_coding_problems/
│   ├── week3_p1.py                  # Remove duplicates from sorted linked list
│   ├── week3_p2.py                  # Doubly linked list — insert_at_pos
│   └── week3_p3.py                  # Merge two sorted linked lists
├── concept_questions/
├── EXPLANATION.md
└── README.md
```

## Topics Covered

| Week | Topics |
|------|--------|
| **Week 1** | Sorting, Sliding Window, Number Theory (Primality Testing) |
| **Week 2** | Stable Sorting, Binary Search, In-Place Merge, Counting Sort |
| **Week 3** | Hash Maps, Stacks (RPN Evaluation), Linked Lists (Singly & Doubly) |
| **Week 3 — Live Coding** | Singly LL duplicate removal, Doubly LL insertion, Merging sorted LLs |

## How to Run

```bash
python -m week1.grpa1_min_difference
python -m week2.ppa1_binary_search
python -m week3.grpa2_evaluate_expression
python -m week3.ppa1_doubly_linked_list

# Live coding problems (run directly, reads from stdin)
python live_coding_problems/week3_p1.py
python live_coding_problems/week3_p2.py
python live_coding_problems/week3_p3.py
```

> **Python 3.10+** is recommended.

## License

This repository is for personal academic reference only.
