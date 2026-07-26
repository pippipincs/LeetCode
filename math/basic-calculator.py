class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(stack):
            res = stack.pop()
            while stack and stack[-1] != ")":
                sign = stack.pop()
                if sign == "+":
                    res += stack.pop()
                elif sign == "-":
                    res -= stack.pop()
            return res
        n = 0
        operand = 0
        stack = []
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]

            if ch.isdigit():
                operand = 10 ** n * int(ch) + operand
                n += 1
            elif ch != " ":
                if n:
                    stack.append(operand)
                    n = 0
                    operand = 0
                if ch == "(":
                    res = evaluate(stack)
                    stack.pop()
                    stack.append(res)

                else:
                    stack.append(ch)
        if n:
            stack.append(operand)
        return evaluate(stack)