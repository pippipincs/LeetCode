class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = collections.Counter(magazine)
        for letter in ransomNote:
            if c[letter] > 0:
                c[letter] -= 1
            else:
                return False
        return True