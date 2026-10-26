# =============================================================================
# WEEK 3 - Problem 1: Remove Duplicates from Sorted Linked List
# =============================================================================
#
# Given class Node:
#   class Node:
#       def __init__(self, data=None):
#           self.data = data   # Stores data
#           self.next = None   # Contains reference to next node, otherwise None
#
# You are given a non-empty linked list with n nodes, sorted in ascending order.
# Your task is to remove nodes with duplicate values from the given list.
#
# Write a function removeDuplicate(head), where head is a reference to the
# first node of the sorted linked list, that removes nodes with duplicate
# values. The function should NOT return any value.
#
# Sample Input:
#   1 1 2 2 2 3 3 4 4 4 4 5 7 9
#
# Output:
#   Output Linked List: 1 2 3 4 5 7 9
# =============================================================================


class Node:
    def __init__(self, data=None):
        self.data = data  # Stores data
        self.next = None  # Contains reference to the next node if it exists, otherwise None


def removeDuplicate(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            current = current.next


# --- Driver code ---
elements = list(map(int, input().split()))

# Build the linked list
head = Node(elements[0])
tail = head
for val in elements[1:]:
    tail.next = Node(val)
    tail = tail.next

# Remove duplicates
removeDuplicate(head)

# Print result
result = []
current = head
while current:
    result.append(str(current.data))
    current = current.next

print("Output Linked List:", " ".join(result))
