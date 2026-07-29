from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for i in range(1, len(words)):
            curr = Counter(words[i])
            for letter in common.keys():
                common[letter] = min(curr[letter], common[letter])
        res = []
        for letter, freq in common.items():
            for _ in range(freq):
                res.append(letter)
        return res
