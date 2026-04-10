class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(stack, visit, i):
            if i in stack:
                return True
            if i in visit:
                return False
            stack.add(i)
            visit.add(i)
            for nei in adj[i]:
                if dfs(stack, visit, nei):
                    return True
            stack.remove(i)
            return False

        stack = set()
        visit = set()

        adj = [[] for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[crs].append(pre)

        for i in range(numCourses):
            if dfs(stack, visit, i):
                return False
        return True