class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
                continue
            elif stack and ((ch == ')' and stack[-1] == '(') or (ch == '}' and stack[-1] == '{') or (ch == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                stack.append(ch)
        return stack == []