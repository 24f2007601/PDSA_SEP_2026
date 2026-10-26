"""
Problem: Implement a Stack using only two Queues.
The implemented Stack should support all the functions of a normal stack:
    push, pop, top, and isempty.

Create the following methods for the class `stack`:

    - push(data) : Insert element `data` to the top of the stack.
    - pop()      : If stack is empty return "Stack is empty".
                   Otherwise, remove the element from the top of the stack and return it.
    - top()      : If stack is empty return "Stack is empty".
                   Otherwise, return the element on the top of the stack.
    - isempty()  : Returns True if the stack is empty, False otherwise.

Sample Input:
    [10, 20, 30, 40, 50]  # push one by one
    2                     # pop 2 elements

Sample Output:
    50   #first popped element
    40   #second popped element
    30   #top element
    False  #isempty
"""

class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, key):
        self.items.insert(0,key)
    def dequeue(self):
        return self.items.pop()

class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0 
    
    def push(self, data):
        self.q1.enqueue(data)
        self.size += 1 
    
    def pop(self):
        if self.size == 0:
            return "Stack is empty"
        while len(self.q1.items) > 1:
            self.q2.enqueue(self.q1.dequeue())
        top = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        self.size -= 1
        return top
    
    def top(self):
        if self.size == 0:
            return "Stack is empty"
        while len(self.q1.items) > 1:
            self.q2.enqueue(self.q1.dequeue())
        top = self.q1.dequeue()
        self.q2.enqueue(top)
        self.q1, self.q2 = self.q2, self.q1
        return top
    
    def isempty(self):
        return self.size == 0



if __name__ == "__main__":
    s = stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.push(50)
    print(s.pop())
    print(s.pop())
    print(s.top())
    print(s.isempty())
    
