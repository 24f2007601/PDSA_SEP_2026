"""GRPA 3 — Reverse a singly linked list in place (pointer rewiring only)."""

from typing import Protocol


class LinkedNode(Protocol):
    """Minimal protocol matching the graded Node interface."""

    value: object
    next: "LinkedNode | None"

    def isEmpty(self) -> bool:  # noqa: N802 — matches original casing
        """Return True if the list rooted at this node is empty."""
        ...


def reverse(root: LinkedNode | None) -> LinkedNode | None:
    """Reverse a singly linked list by rewiring next pointers.

    Only the ``next`` pointers of existing nodes are changed.
    No new nodes are created and no values are modified.

    Args:
        root: The head node of the linked list, or ``None`` for an empty list.

    Returns:
        The new head node (previously the tail), or ``None`` for an empty list.

    Time:  O(n)  — single pass through the list
    Space: O(1)  — three pointer variables only
    """
    prev: LinkedNode | None = None
    current = root

    while current is not None:
        next_node = current.next  # save successor before overwriting
        current.next = prev       # reverse the pointer
        prev = current            # advance prev
        current = next_node       # advance current

    return prev
