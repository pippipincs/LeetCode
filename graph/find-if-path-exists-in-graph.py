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
        root_u = self.find(u)
        root_v = self.find(v)

        if u!= v:
            self.parent[root_u] = root_v
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for i, j in edges:
            uf.join(i, j)
        return uf.isSame(source, destination)
