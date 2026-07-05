class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        suppliesset = set(supplies)
        g = collections.defaultdict(list)
        indegree = [0] * len(recipes)
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                if ingredient not in suppliesset:
                    g[ingredient].append(i)
                    indegree[i] += 1
        queue = deque([idx for idx, v in enumerate(indegree) if v == 0])
        while queue:
            completedRecipe = queue.popleft()
            res.append(recipes[completedRecipe])

            for dependent in g[recipes[completedRecipe]]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        return res
        
