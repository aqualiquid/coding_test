class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        n = len(s)
        cur = prev = res = 0
        op = '+'

        while i < n:
            if s[i].isdigit():
                cur = 0
                while i < n and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                if op == '+':
                    res += cur
                    prev = cur
                elif op == '-':
                    res -= cur
                    prev = -cur
                elif op == '*':
                    res -= prev
                    prev = prev * cur
                    res += prev
                elif op == '/':
                    res -= prev
                    prev = int(prev / cur)
                    res += prev
                else:
                    print("Invalid operator")
            elif s[i] != " ":
                op = s[i]
                i += 1
            else:
                i += 1
        return res