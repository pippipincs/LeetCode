class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, u):
        if u == self.parent[u]:
             return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]
    def isSame(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        return root_u == root_v
    def join(self, u, v):
        if u == v:
            return
        root_u = self.find(u)
        root_v = self.find(v)
        self.parent[root_u] = root_v
class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        for a, b in edges:
            if not uf.isSame(a, b):
                uf.join(a, b)
            else:
                return [a, b]
        