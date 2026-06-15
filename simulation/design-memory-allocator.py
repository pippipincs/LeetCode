class Allocator:

    def __init__(self, n: int):
        self.memory = [False] * n
        self.blocks = collections.defaultdict(list)
        self.n = n

    def allocate(self, size: int, mID: int) -> int:
        for leftmost in range(self.n - size + 1):
            if self.memory[leftmost]:
                continue
            else:
                available = True
                for i in range(leftmost, leftmost + size ):
                    if self.memory[i]:
                        available = False
                        break
                if not available:
                    continue
                else:
                    self.memory[leftmost : leftmost + size ] = [True] * size

                    self.blocks[mID].append((leftmost, size))
                    return leftmost
        return -1

    def freeMemory(self, mID: int) -> int:
        
        total = 0
        for first, size in self.blocks[mID]:
            self.memory[first : first + size ] = [False] * size
            total += size

        self.blocks[mID] = []
        return total


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)