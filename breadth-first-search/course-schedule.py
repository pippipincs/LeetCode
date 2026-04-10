class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for pre, crs in prerequisites:
            adj[crs].append(pre)
            indegree[pre] += 1
        from collections import deque

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        visitedNode = 0

        while q:
            curr = q.popleft()
            visitedNode += 1
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return visitedNode == numCourses

