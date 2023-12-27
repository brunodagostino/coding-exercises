class Queue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []
    
    def is_empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
    
    def peek(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]
    
    def add(self, data) -> None:
        self.stack1.append(data)
    
    def remove(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        data = self.stack2.pop()

        return data


# Test cases
queue = Queue()
queue.add(data=42)
queue.remove()
queue.add(data=14)
n = queue.peek()
print(n)
queue.add(data=28)
n = queue.peek()
print(n)
queue.add(data=60)
queue.add(data=78)
queue.remove()
queue.remove()