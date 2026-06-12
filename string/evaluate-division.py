class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = collections.defaultdict(list)
        for i, (s, e) in enumerate(equations):
            g[s].append((e, values[i]))
            g[e].append((s, 1 / values[i]))
        res = []
        def calculate(a, b, visited):
            if a not in g.keys() or b not in g.keys():
                return -1
            visited.add(a)
            if a == b:
                return 1
            for nei, v in g[a]:
                if nei not in visited:
                    dis = calculate(nei, b, visited) 
                    if dis != -1:
                        return dis * v
                    else:
                        continue
            return -1
                    
        for a, b in queries:
            visited = set()
            res.append(calculate(a, b, visited))
        return res