"""
Merge two sorted linked list
=============================

class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Contains reference to the next node if it exists, otherwise None

Consider an implementation of a linked list, where each node is created using the given
class Node. Suppose it has a head variable that contains the reference to the first node
of the linked list.

You are given two non-empty linked lists with n and m nodes, where these nodes are sorted
in ascending order of their value. Your task is to merge these two sorted linked lists
into one sorted linked list.

Write a function mergeSortedList(head1, head2), where head1 and head2 are references to
the first nodes of two sorted linked lists. The function should return the reference of
the first node of the merged sorted linked list.

Sample Input:
    1 3 5 7 9 11  #Elements of first linked list
    2 4 6         #Elements of second linked list

Output:
    Output Linked List: 1 2 3 4 5 6 7 9 11  #Elements of merged sorted linked list
"""


class Node:
    def __init__(self, data):
        self.data = data  # Stores data
        self.next = None  # Contains reference to the next node if it exists, otherwise None


def mergeSortedList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        head1.next = mergeSortedList(head1.next, head2)  # link remaining
        return head1
    else:
        head2.next = mergeSortedList(head1, head2.next)  # link remaining
        return head2


if __name__ == "__main__":
    l1 = Node(1)
    l1.next = Node(3)
    l1.next.next = Node(5)
    l1.next.next.next = Node(7)
    l1.next.next.next.next = Node(9)
    l1.next.next.next.next.next = Node(11)

    l2 = Node(2)
    l2.next = Node(4)
    l2.next.next = Node(6)

    merged = mergeSortedList(l1, l2)
    while merged:
        print(merged.data, end=" ")
        merged = merged.next


