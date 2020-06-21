# Classic Interview Problem
'''
Implementation of Queue using Two Stacks

Logic:
      We need to understand that stack reverses the order while queue doesn't.
      Means, when we pop previously pushed elements, they come back in a
      reversed order.

Example : s = Stack()
          s.push(1) s.push(2) s.push(3)
          s.pop() -> 3
          s.pop() -> 2
          s.pop() -> 1

     If we use two stacks chained together, we"ll be able to return
     elements in the same order, since reversed order reversed again
     is original order.

Example : s1 = Stack()
          s1.push(s.pop()) s1.push(s.pop()) s1.push(s.pop())
          s1.pop() -> 1
          s1.pop() -> 2
          s1.pop() -> 3
'''

class QUsing2Stacks():

    def __init__(self):
        # Stack works same as list
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        # Add elements to the instack
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                # add the elements to the outstack
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = QUsing2Stacks()
for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())