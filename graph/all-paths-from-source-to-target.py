class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        result = []
        def dfs(path, i):
            if i == n - 1:
                result.append(path.copy())
                return
            for j in graph[i]:
                path.append(j)
                dfs(path, j)
                path.pop()
        dfs([0], 0)
        return result
            