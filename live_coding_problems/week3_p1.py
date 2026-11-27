"""
Remove duplicate from sorted linked list.

Given a non-empty linked list with n nodes sorted in ascending order,
remove nodes with duplicate values in place. The function should not return any value.
"""

from typing import Any, Optional


class Node:
    def __init__(self, data: Any = None) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


def removeDuplicate(head: Optional[Node]) -> None:
    """Remove duplicate values from a sorted singly linked list in-place."""
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next


if __name__ == "__main__":
    def build_list(vals: list[int]) -> Optional[Node]:
        if not vals:
            return None
        head = Node(vals[0])
        curr = head
        for val in vals[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head

    def to_list(head: Optional[Node]) -> list[int]:
        res = []
        curr = head
        while curr:
            res.append(curr.data)
            curr = curr.next
        return res

    # Sample input test
    test_vals = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 7, 9]
    h = build_list(test_vals)
    removeDuplicate(h)
    assert to_list(h) == [1, 2, 3, 4, 5, 7, 9]

    # Edge cases: single element, all duplicates
    h_single = build_list([5])
    removeDuplicate(h_single)
    assert to_list(h_single) == [5]

    h_same = build_list([2, 2, 2])
    removeDuplicate(h_same)
    assert to_list(h_same) == [2]

    print("All checks passed.")
