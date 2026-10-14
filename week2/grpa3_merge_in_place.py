"""GRPA 3 — Merge two sorted MyList arrays in place (swap-only constraint)."""

from typing import Protocol


class SwappableList(Protocol):
    """Minimal protocol matching the MyList swap interface."""

    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> int: ...
    def swap(self, index_self: int, other: "SwappableList", index_other: int) -> None: ...


def merge_in_place(a: SwappableList, b: SwappableList) -> None:
    """Merge two sorted SwappableLists so `a` holds the smallest elements.

    After merging, `a` contains the smallest len(a) values and `b` the rest,
    both in ascending order. Uses only the `.swap()` method for mutation.

    Time:  O(n × m)  where n = len(a), m = len(b)
    """
    n = len(a)
    m = len(b)

    if n == 0 or m == 0:
        return

    for i in range(n):
        if a[i] > b[0]:
            a.swap(i, b, 0)

            j = 0
            while j < m - 1 and b[j] > b[j + 1]:
                b.swap(j, b, j + 1)
                j += 1
