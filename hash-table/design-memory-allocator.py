class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.memory[i]:
                cnt = 0
                continue
            else:
                cnt += 1
            if cnt == size:
                start = i - size + 1
                self.memory[start : i + 1] = [mID] * size
                return start
        return -1

    def freeMemory(self, mID: int) -> int:
        cnt = 0
        for i in range(self.n):
            if self.memory[i] == mID:
                cnt += 1
                self.memory[i] = 0
        return cnt


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)