"""
Problem — Find Pair with Target Sum (O(n log n))
=================================================
Given a list L of random numbers and a target pairSum, return True if any two
elements in L sum to pairSum, else False.

Sample Input 1 : 10 4 11 5 1 8 7 / 21  →  True  (11 + 10)
Sample Input 2 : 10 4 11 5 1 8 7 / 2   →  False
"""


def findPair(L: list[int], pairSum: int) -> bool:
    """Return True if any two distinct elements in L sum to pairSum — O(n log n)."""
    sorted_L = sorted(L)
    left, right = 0, len(sorted_L) - 1

    while left < right:
        current_sum = sorted_L[left] + sorted_L[right]
        if current_sum == pairSum:
            return True
        if current_sum < pairSum:
            left += 1
        else:
            right -= 1

    return False


L = list(map(int, input().split()))
pair_sum = int(input())
print(findPair(L, pair_sum))
