"""PPA 1 — Doubly linked list with O(1) insert_end and delete_end."""


class Node:
    """A single node in a doubly linked list."""

    def __init__(self, data: int) -> None:
        self.data = data          # stored value
        self.next: "Node | None" = None   # reference to the next node
        self.prev: "Node | None" = None   # reference to the previous node


class doubly_linked_list:  # noqa: N801 — matches original graded class name
    """A doubly linked list with O(1) tail insertion and deletion.

    Maintains explicit ``head`` and ``last`` pointers so that both
    ``insert_end`` and ``delete_end`` run in constant time without
    traversing the list.
    """

    def __init__(self) -> None:
        self.head: Node | None = None   # first node in the list
        self.last: Node | None = None   # last node in the list

    # ------------------------------------------------------------------
    # Mutations
    # ------------------------------------------------------------------

    def insert_end(self, data: int) -> None:
        """Append a new node with ``data`` at the tail in O(1)."""
        new_node = Node(data)
        if self.head is None:
            # List was empty — new node becomes both head and tail.
            self.head = new_node
            self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node  # type: ignore[union-attr]
            self.last = new_node

    def delete_end(self) -> None:
        """Remove the tail node in O(1). No-op on an empty list."""
        if self.head is None:
            return

        if self.head is self.last:
            # Only one node — list becomes empty.
            self.head = None
            self.last = None
            return

        self.last = self.last.prev       # type: ignore[union-attr]
        self.last.next = None            # type: ignore[union-attr]

    # ------------------------------------------------------------------
    # Traversal helpers
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """Return comma-separated values from head to tail."""
        parts: list[str] = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        return ",".join(parts)

    def to_string_reverse(self) -> str:
        """Return comma-separated values from tail to head."""
        parts: list[str] = []
        current = self.last
        while current is not None:
            parts.append(str(current.data))
            current = current.prev
        return ",".join(parts)
