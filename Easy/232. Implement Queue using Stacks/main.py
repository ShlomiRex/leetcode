class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) != 0:
            val = self.stack1.pop()
            self.stack2.append(val)
        ret = self.stack2.pop() # Pop last element - which is front of queue
        while len(self.stack2) != 0:
            val = self.stack2.pop()
            self.stack1.append(val)
        return ret

    def peek(self) -> int:
        while len(self.stack1) != 0:
            val = self.stack1.pop()
            self.stack2.append(val)
        ret = self.stack2.pop()
        self.stack2.append(ret) # Return the value back
        while len(self.stack2) != 0:
            val = self.stack2.pop()
            self.stack1.append(val)
        return ret

    def empty(self) -> bool:
        return len(self.stack1) == 0

# Your MyQueue object will be instantiated and called as such:


if __name__ == "__main__":
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    assert obj.pop() == 1
    assert obj.pop() == 2
    
    obj.push(1)
    obj.push(2)
    assert obj.empty() == False
    assert obj.peek() == 1
    assert obj.peek() == 1
    assert obj.empty() == False
    obj.pop()
    obj.pop()
    assert obj.empty() == True
