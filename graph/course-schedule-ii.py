class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        g = collections.defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indegree[a] += 1
        res = []
        queue = deque()
        for i, d in enumerate(indegree):
            if d == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for nei in g[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res) == numCourses else []