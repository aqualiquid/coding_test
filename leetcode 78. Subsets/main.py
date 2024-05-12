from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path.copy())

            for end in range(start, len(nums)):
                path.append(nums[end])
                backtrack(end+1, path)
                path.pop()


        result = []
        backtrack(0, [])
        return result