class Solution:
    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char not in table:
                stack.append(c)
                continue
            if not stack and stack[-1] != table:
                return False
