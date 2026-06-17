class Solution:
    def calculate(self, s: str) -> int:
        
        n = len(s)
        operations = "+"
        curr = 0
        last = 0
        res = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == n - 1:
                if operations == "+":
                    
                    res += last
                    last = curr
                if operations == "-":
                    res += last
                    last = -curr
                if operations == "*":
                    last = last * curr
                if operations == "/":
                    last = int(last / curr)
                operations = ch
                curr = 0
        res += last
        return res