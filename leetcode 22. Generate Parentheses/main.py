from typing import List


class Solution:
    def backtrack(self, res, cur, close_cnt, open_cnt, n):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if open_cnt < n:
            self.backtrack(res, cur + '(', close_cnt, open_cnt + 1, n)
        if open_cnt > close_cnt:
            self.backtrack(res, cur + ')', close_cnt + 1, open_cnt, n)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, '', 0, 0, n)
        return res


