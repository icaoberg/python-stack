class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.insert(0,element)

    def pop(self):
        answer = self.elements[-1]
        self.elements = self.elements[:-1]
        return answer

    def peek(self):
        return self.elements[-1]

    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.elements)
