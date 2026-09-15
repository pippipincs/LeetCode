class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        transformation = collections.defaultdict(list)
        for word in wordList:
            for i in range(L):
                transformation[word[:i] + "*" + word[i+ 1:]].append(word)
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while queue:
            current, level = queue.popleft()
            for i in range(L):
                for nextword in transformation[current[:i] + "*" + current[i + 1:]]:
                    if nextword == endWord:
                        return level + 1
                    if nextword not in visited:
                        visited.add(nextword)
                        queue.append((nextword, level + 1))
                transformation[current[:i] + "*" + current[i + 1:]] = []
        return 0