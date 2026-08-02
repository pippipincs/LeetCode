class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.topv = 0

    def push(self, x: int) -> None:
        if self.empty():
            self.q1.append(x)
        elif self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)
        self.topv = x

    def pop(self) -> int:
        if not self.q2:
            while len(self.q1) > 2:
                x = self.q1.popleft()
                self.q2.append(x)
            if len(self.q1) == 2:
                self.topv = self.q1.popleft()
                self.q2.append(self.top)
            return self.q1.popleft()
        else:
            while len(self.q2) > 1:
                x = self.q2.popleft()
                self.q1.append(x)
            if len(self.q2) == 2:
                self.topv = self.q2.popleft()
                self.q1.append(self.top)
            return self.q2.popleft()
        

    def top( self) -> int:
        return self.topv

    def empty(self) -> bool:
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()