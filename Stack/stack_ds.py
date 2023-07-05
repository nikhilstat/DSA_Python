class Stack_with_list:
    """
    Stack implementation using a list.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.stack = []

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.stack == []

    def push(self, data):
        """
        Push an element onto the stack.

        Args:
            data: The element to be pushed onto the stack.
        """
        self.stack.append(data)

    def pop(self):
        """
        Remove and return the top element from the stack.

        Returns:
            The top element of the stack.
        """
        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def peek(self):
        """
        Get the value of the top element without removing it.

        Returns:
            The value of the top element.
        """
        return self.stack[-1]

    def size_stack(self):
        """
        Get the size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)


from collections import deque


class Stack_with_deque:
    """
    Stack implementation using a deque from the collections module.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.stack = deque()

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return bool(self.stack)

    def push(self, data):
        """
        Push an element onto the stack.

        Args:
            data: The element to be pushed onto the stack.
        """
        self.stack.append(data)

    def pop(self):
        """
        Remove and return the top element from the stack.
        """
        self.stack.pop()

    def peek(self):
        """
        Get the value of the top element without removing it.

        Returns:
            The value of the top element.
        """
        return self.stack[-1]

    def size_stack(self):
        """
        Get the size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.stack)


from queue import LifoQueue


class Stack_with_queue:
    """
    Stack implementation using LifoQueue from the queue module.
    """

    def __init__(self, maxsize=2):
        """
        Initialize an empty stack with a maximum size.

        Args:
            maxsize (int): The maximum size of the stack.
        """
        self.stack = LifoQueue(maxsize=maxsize)

    def __repr__(self):
        """
        Get the string representation of the stack.

        Returns:
            str: The string representation of the stack.
        """
        values = list(self.stack.queue)
        return f"Stack: {values}"

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.stack.empty()

    def push(self, data):
        """
        Push an element onto the stack.

        Args:
            data: The element to be pushed onto the stack.
        """
        self.stack.put(data)

    def pop(self):
        """
        Remove and return the top element from the stack.
        """
        self.stack.get()

    def peek(self):
        """
        Get the value of the top element without removing it.

        Returns:
            The value of the top element.
        """
        if not self.is_empty():
            last_element = self.stack.get()
            self.stack.put(last_element)
            return last_element

    def size_stack(self):
        """
        Get the size of the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return self.stack.qsize()
