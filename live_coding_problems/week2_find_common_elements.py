"""
Problem — Find Common Elements (O(n log n), no sets)
=====================================================
Write a function findCommonElements(L1, L2) that accepts two integer lists of the
same length n (each with all distinct values) and returns a list of elements that
appear in both. The returned list may be in any order.

Do NOT use Python's built-in set.

Sample Input 1:
  L1 = [23, 24, 18, 22, 20, 10, 17, 12, 16, 19, 21, 15, 14, 11, 13]
  L2 = [23, 22, 33, 24, 31, 21, 20, 26, 30, 29, 25, 27, 28, 34, 32]
  Output: [20, 21, 22, 23, 24]

Sample Input 2:
  L1 = [3, 7, 2, 9, 5]   L2 = [6, 3, 7, 5, 4]
  Output: [3, 5, 7]
"""

from typing import Sequence


def findCommonElements(L1: Sequence[int], L2: Sequence[int]) -> list[int]:
    """Return elements common to L1 and L2 using sort + two-pointer — O(n log n)."""
    sorted1 = sorted(L1)
    sorted2 = sorted(L2)
    common: list[int] = []
    i = j = 0

    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] == sorted2[j]:
            common.append(sorted1[i])
            i += 1
            j += 1
        elif sorted1[i] < sorted2[j]:
            i += 1
        else:
            j += 1

    return common


def _parse_list(line: str) -> list[int]:
    return list(map(int, line.strip().strip("[]").split(",")))


L1 = _parse_list(input())
L2 = _parse_list(input())
print(findCommonElements(L1, L2))
