from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking approach : (1) recusrive, (2) combination, (3) serise, (4) subets
        results = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                results.append(list(combination))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combination.append(candidate)
                backtrack(remaining - candidate, combination, i)
                combination.pop()

        backtrack(target, [], 0)
        return results