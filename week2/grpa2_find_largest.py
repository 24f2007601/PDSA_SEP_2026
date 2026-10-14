"""GRPA 2 — Largest element in a sorted-and-rotated list (binary search)."""


def find_largest(numbers: list[int]) -> int:
    """Return the largest element in a sorted-then-rotated list using binary search.

    Finds the pivot point (where the sorted order breaks) in O(log n).
    Does not use list slicing.

    Time:  O(log n)
    """
    low = 0
    high = len(numbers) - 1

    if numbers[low] <= numbers[high]:
        return numbers[high]

    while low <= high:
        mid = (low + high) // 2

        if mid < len(numbers) - 1 and numbers[mid] > numbers[mid + 1]:
            return numbers[mid]
        if mid > 0 and numbers[mid] < numbers[mid - 1]:
            return numbers[mid - 1]

        if numbers[mid] >= numbers[low]:
            low = mid + 1
        else:
            high = mid - 1

    return numbers[low]
