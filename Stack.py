class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.elements.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def tolist(self):
        return list(self.elements)

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return f"Stack({self.elements})"
