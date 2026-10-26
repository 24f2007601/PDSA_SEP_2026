"""
Problem — Find Peak Element (O(log n))
======================================
Write a function Findpeak(L) that accepts a list L of n distinct elements and
returns the peak element. A peak is greater than both its neighbours; for corner
elements, only one neighbour is considered. Exactly one peak exists in L.

Sample Input 1 : 5 10 20 15   →  Output: 20
Sample Input 2 : 1 2 3 4 5 6 7 8  →  Output: 8
"""

from typing import Optional


def Findpeak(L: list[int]) -> Optional[int]:
    """Return the peak element of L using binary search — O(log n)."""
    n = len(L)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2
        left_ok = mid == 0 or L[mid] > L[mid - 1]
        right_ok = mid == n - 1 or L[mid] > L[mid + 1]

        if left_ok and right_ok:
            return L[mid]
        if mid > 0 and L[mid - 1] > L[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


L = list(map(int, input().split()))
print(Findpeak(L))