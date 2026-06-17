class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        operations = "+"
        curr = 0
        for i, ch in enumerate(s):
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == n - 1:
                if operations == "+":
                    stack.append(curr)
                if operations == "-":
                    stack.append(-curr)
                if operations == "*":
                    stack.append(stack.pop() * curr)
                if operations == "/":
                    stack.append(int(stack.pop() / curr))
                operations = ch
                curr = 0
        return sum(stack)