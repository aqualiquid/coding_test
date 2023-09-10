from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def backtracking(path, idx):
            if idx == len(s):
                res.append("".join(path))
                return

            if s[idx].isdigit():
                path.append(s[idx])
                backtracking(path, idx+1)
                path.pop()

            else:
                path.append(s[idx].lower())
                backtracking(path, idx + 1)
                path.pop()

                path.append(s[idx].upper())
                backtracking(path, idx + 1)
                path.pop()

        res = []
        backtracking([], 0)
        return res