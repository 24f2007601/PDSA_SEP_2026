def find_first_eligible(status: list[int]) -> int:
    """
    Find the index of the first student with status 1 in a sorted binary list.

    The list contains only 0s followed by 1s (sorted order guaranteed).
    Uses binary search to achieve O(log n) time complexity.

    Args:
        status: A sorted list of 0s and 1s.

    Returns:
        Zero-based index of the first 1, or -1 if no 1 exists.
    """
    lo, hi = 0, len(status) - 1
    first_eligible = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if status[mid] == 1:
            first_eligible = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return first_eligible


# -- Test cases ----------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([0, 0, 0, 1, 1, 1], 3),
        ([0, 0, 1, 1, 1],    2),
        ([1, 1, 1, 1, 1, 1], 0),
        ([0, 0, 0, 0, 0],   -1),
    ]

    for status, expected in test_cases:
        result = find_first_eligible(status)
        icon = "PASS" if result == expected else "FAIL"
        print(f"[{icon}] Input: {status} -> Output: {result}  (expected: {expected})")
