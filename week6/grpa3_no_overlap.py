"""
A popular meeting hall in a city receives many overlapping applications to hold meetings. The manager wishes to satisfy as many customers as possible. Each application is a tuple (id, start_day, end_day) where id, start_day and end_day are the unique id assigned to the application, starting day of the meeting and ending day of meeting ends inclusive respectively.

Write a function no_overlap(L) to return the list of customer ids whose applications are accepted that ensures optimal scheduling. Let L be a list tuples with (id, start_day, end_day).

Sample Input

L = [
    (0, 1, 2),
    (1, 1, 3),
    (2, 1, 5),
    (3, 3, 4),
    (4, 4, 5),
    (5, 5, 8),
    (6, 7, 9),
    (7, 10, 13),
    (8, 11, 12)
]
Sample output

[0, 3, 6, 8]
 """


def no_overlap(L: list[tuple[int, int, int]]) -> list[int]:
    """Return customer ids for maximum non-overlapping meetings (earliest end first)."""
    accepted = []
    last_end = float("-inf")
    for cid, start, end in sorted(L, key=lambda x: x[2]):
        if start > last_end:
            accepted.append(cid)
            last_end = end
    return accepted


if __name__ == "__main__":
    sample = [
        (0, 1, 2), (1, 1, 3), (2, 1, 5), (3, 3, 4), (4, 4, 5),
        (5, 5, 8), (6, 7, 9), (7, 10, 13), (8, 11, 12),
    ]
    res = no_overlap(sample)
    assert len(res) == 4
    assert no_overlap([]) == []
    print("All checks passed:", res)