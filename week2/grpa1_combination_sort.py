"""GRPA 1 — Combination sort (stable letter sort + descending number sort)."""


def combination_sort(str_list: list[str]) -> tuple[list[str], list[str]]:
    """Sort letter-number strings by character stability and numeric order.

    Returns two lists:
      L1 — sorted by first character only (stable, preserves original order within ties).
      L2 — sorted by first character ascending, then by numeric suffix descending.

    Time:  O(n log n)
    """
    by_letter = sorted(str_list, key=lambda s: s[0])
    by_letter_and_number = sorted(str_list, key=lambda s: (s[0], -int(s[1:])))

    return by_letter, by_letter_and_number
