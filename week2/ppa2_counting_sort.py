"""PPA 2 — Counting sort for integers in a bounded range [0, r)."""


def sort_in_range(numbers: list[int], upper_bound: int) -> None:
    """Sort `numbers` in place using counting sort.

    Every element must satisfy 0 <= element < upper_bound.

    Time:  O(n + r)  where n = len(numbers), r = upper_bound
    Space: O(r)      for the counts array
    """
    counts = [0] * upper_bound
    for num in numbers:
        counts[num] += 1

    index = 0
    for value in range(upper_bound):
        for _ in range(counts[value]):
            numbers[index] = value
            index += 1
