#question 
"""
A doubly linked list is a linked data structure that consists of two header nodes that point to the first and last position in a sequence of linked records. Each node in the sequence contains three fields: One data field and two link fields (references to the previous and to the next node in the sequence of nodes) and. So, it can be traversed in both directions.

For the given class doubly_linked_list, create two methods:

insert_end(data): that accepts an integer data and inserts it into the list at the last position.
delete_end(): Delete one element of the list from the last position.
Note- Use given linked list structure to implementation. Write both operations (insert_end and delete_end) with O(1) time.

class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains the reference of next node
        self.prev = None # Contains the reference of previous node
class doubly_linked_list:
    def __init__(self):
        self.head = None # Contains the reference of first node of the list
        self.last = None # Contains the reference of the last node of the list
Example



Sample Input

[1,3,5,7,9] # Elements for insert in list one by one, start from 1
2 # Perform delete_end operation two times
Output

1,3,5 # Traversed list from head to last after deleting two elements
5,3,1 # Traversed list from last to head after deleting two elements
"""

class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains the reference of next node
        self.prev = None # Contains the reference of previous node
class doubly_linked_list:
    def __init__(self):
        self.head = None # Contains the reference of first node of the list
        self.last = None # Contains the reference of the last node of the list
    
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

    def delete_end(self):
        if self.head is None:
            return
        if self.head == self.last:
            self.head = None
            self.last = None
            return
        self.last = self.last.prev
        self.last.next = None
    def __str__(self):
        if self.head is None:
            return ""
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += ","
            current = current.next
        return result