"""
Problem — Merge Sort Subordinates
==================================
A deck of cards (integers 0–100,000,000) is distributed through a binary tree
of subordinates modelled after merge sort:
  - Each node splits its deck in half and delegates to two subordinates.
  - A subordinate with 2 cards sorts and returns them.
  - A subordinate with 1 card returns it as-is.
  - Each node merges the two sorted halves it receives.

Write def subordinates(L) returning (sorted_list, number_of_people_involved).

Sample Input 1: [194, 69, 103, 150, 151, 44, 103, 98]
Output:         ([44, 69, 98, 103, 103, 150, 151, 194], 7)

Sample Input 2: [10, 33, 45, 67, 92, 100, 5]
Output:         ([5, 10, 33, 45, 67, 92, 100], 7)
"""

SINGLE_PERSON_COUNT = 1


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list — O(n)."""
    result: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def subordinates(L: list[int]) -> tuple[list[int], int]:
    """Return (sorted L, total people in the recursion tree) — O(n log n)."""
    n = len(L)
    if n <= 1:
        return (L, SINGLE_PERSON_COUNT)
    if n == 2:
        return (sorted(L), SINGLE_PERSON_COUNT)

    mid = n // 2
    left_sorted, left_count = subordinates(L[:mid])
    right_sorted, right_count = subordinates(L[mid:])

    return (_merge(left_sorted, right_sorted), SINGLE_PERSON_COUNT + left_count + right_count)


L = list(map(int, input().strip().strip("[]").split(",")))
print(subordinates(L))
