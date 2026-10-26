# =============================================================================
# WEEK 3 - Problem 2: Doubly Linked List - insert_at_pos
# =============================================================================
#
# A doubly linked list is a linked data structure that consists of a set of
# sequentially linked records called nodes. Each node contains three fields:
# two link fields (references to the previous and to the next node in the
# sequence of nodes) and one data field. So, it can be traversed in both
# directions.
#
# For the given class doubly_linked_list, create one method:
#
#   insert_at_pos(data, pos):
#       Accepts an integer `data` and inserts it into the list at given `pos`
#       position where  1 < pos <= length(list)
#
# Note: Use the given linked list structure for implementation.
#
# Given structure:
#   class Node:
#       def __init__(self, data):
#           self.data = data   # Stores data
#           self.next = None   # Contains the reference of next node
#           self.prev = None   # Contains the reference of previous node
#
#   class doubly_linked_list:
#       def __init__(self):
#           self.head = None   # Contains the reference of first node of the list
#           self.last = None   # Contains the reference of the last node of the list
#
# Example:
#   head --> [None | 10 | -->] <--> [<-- | 20 | -->] <--> [<-- | 30 | None] <-- last
#
# Sample Input:
#   [1,3,5,7,9]   # Elements inserted one by one, starting from index 1
#   20            # data
#   2             # position
#
# Output:
#   1 20 3 5 7 9
# =============================================================================

class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Contains the reference of next node
        self.prev = None  # Contains the reference of previous node


class doubly_linked_list:
    def __init__(self):
        self.head = None  # Contains the reference of first node of the list
        self.last = None  # Contains the reference of the last node of the list

    def insert_at_pos(self, data, pos):
        """
        Insert a node with given data at position pos.
        Constraint: 1 < pos <= length(list)
        """
        new_node = Node(data)

        # Traverse to the node at position (pos - 1)
        current = self.head
        count = 1
        while count < pos - 1:
            current = current.next
            count += 1

        # current is now at position (pos - 1)
        next_node = current.next

        # Link new_node into the list
        new_node.prev = current
        new_node.next = next_node
        current.next = new_node

        if next_node is not None:
            next_node.prev = new_node
        else:
            # Inserted at the tail
            self.last = new_node

    def print_list(self):
        """Print all elements from head to last."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" ".join(elements))


# --- Driver code ---
raw = input().strip().strip("[").strip("]")
elements = list(map(int, raw.split(",")))

data = int(input())
pos  = int(input())

# Build the doubly linked list
dll = doubly_linked_list()
first = Node(elements[0])
dll.head = first
dll.last = first

for i in range(1, len(elements)):
    tail_node = Node(elements[i])
    dll.last.next = tail_node
    tail_node.prev = dll.last
    dll.last = tail_node

# Insert at position
dll.insert_at_pos(data, pos)

# Print result
dll.print_list()
