class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = 0

    def push(self, x: int) -> None:
        if self.stack1 == []:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2 == []:
            return self.front
        else:
            return self.stack2[-1]

    def empty(self) -> bool:
        return self.stack1 == [] and self.stack2 == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()