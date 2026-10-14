"""PPA 1 — Binary search with comparison count."""


def binary_search_with_comparisons(
    sorted_list: list[int], target: int
) -> tuple[bool, int]:
    """Search for `target` in `sorted_list` and count element comparisons.

    Returns (found, num_comparisons) where `num_comparisons` is how many
    elements of `sorted_list` were actually compared to `target`.

    Uses (left + right) // 2 for the midpoint.

    Time:  O(log n)
    """
    left = 0
    right = len(sorted_list) - 1
    num_comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        num_comparisons += 1

        if sorted_list[mid] == target:
            return (True, num_comparisons)
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return (False, num_comparisons)
