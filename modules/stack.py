class Stack:
    def __init__(self):
        self._stack = [] #attribute of the method
    
    def is_empty(self):
        return len(self._stack) == 0

    def push(self, val):
        self._stack.append(val)
    
    def pop(self):
        self._stack.pop()
    
    def top(self):
        return self._stack[-1]