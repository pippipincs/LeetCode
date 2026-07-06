class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        g = collections.defaultdict(list)
        for a, b in prerequisites:
            g[b].append(a)
            indegree[a] += 1
        
        queue = deque([i for i, v in enumerate(indegree) if v == 0])
        while queue:
            crs = queue.popleft()
            for nextcrs in g[crs]:
                indegree[nextcrs] -= 1
                if indegree[nextcrs] == 0:
                    queue.append(nextcrs)
        for v in indegree:
            if v != 0:
                return False
        return True

        