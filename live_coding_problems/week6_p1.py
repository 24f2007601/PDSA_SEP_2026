"""
Identify heap type.

Write a function Type_of_heap(A) that accepts a heap array A and returns:
- 'Max' if input heap is a max heap
- 'Min' if input heap is a min heap
- 'None' otherwise (string 'None' as specified in sample output)
"""

from typing import Any, Sequence


def Type_of_heap(A: Sequence[Any]) -> str:
    """Return 'Max', 'Min', or 'None' indicating the heap property of array A."""
    n = len(A)
    is_min = True
    is_max = True

    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            if A[i] > A[left]:
                is_min = False
            if A[i] < A[left]:
                is_max = False

        if right < n:
            if A[i] > A[right]:
                is_min = False
            if A[i] < A[right]:
                is_max = False

        if not is_min and not is_max:
            return "None"

    if is_max:
        return "Max"
    if is_min:
        return "Min"
    return "None"


if __name__ == "__main__":
    # Sample input 1
    assert Type_of_heap([1, 2, 3, 4, 5, 6]) == "Min"

    # Sample input 2
    assert Type_of_heap([5, 3, 4, 2, 1]) == "Max"

    # Sample input 3
    assert Type_of_heap([1, 5, 4, 7, 6, 3, 2]) == "None"

    # Single element / empty edge cases
    assert Type_of_heap([42]) == "Max"
    assert Type_of_heap([]) == "Max"

    print("All checks passed.")
