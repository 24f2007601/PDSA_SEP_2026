"""GRPA 1 — Minimum difference among P elements (sliding window on sorted list)."""


def find_min_difference(numbers: list[int], subset_size: int) -> int:
    """Return the minimum max-min difference across all subsets of `subset_size` elements.

    Sorts a copy of `numbers`, then slides a window of `subset_size` to find
    the contiguous group with the smallest range.

    Time:  O(n log n)
    Space: O(n) for the sorted copy
    """
    if subset_size > len(numbers):
        return 0

    sorted_numbers = sorted(numbers)
    min_diff = float("inf")

    for i in range(len(sorted_numbers) - subset_size + 1):
        diff = sorted_numbers[i + subset_size - 1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff

    return int(min_diff)
