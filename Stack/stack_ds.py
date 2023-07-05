class Stack_with_list:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        last_item =  self.stack[-1]
        del self.stack[-1]
        return last_item
    
    def peek(self):
        return self.stack[-1]
    
    def size_stack(self):
        return len(self.stack)
    
from collections import deque

class Stack_with_deque:
    def __init__(self):
        self.stack = deque()
        
    def is_empty(self):
        return bool(self.stack)
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        self.stack.pop()
        
    def peek(self):
        return self.stack[-1]
    
    def size_stack(self):
        return len(self.stack)


from queue import LifoQueue

class Stack_with_queue:
    def __init__(self, maxsize=2):
        self.stack = LifoQueue(maxsize=maxsize)
        
    def __repr__(self):
        values = list(self.stack.queue)
        return f"Stack: {values}"

    def is_empty(self):
        return self.stack.empty()

    def push(self, data):
        self.stack.put(data)

    def pop(self):
        self.stack.get()

    def peek(self):
        if not self.is_empty():
            last_element = self.stack.get()
            self.stack.put(last_element)
            return last_element

    def size_stack(self):
        return self.stack.qsize()
