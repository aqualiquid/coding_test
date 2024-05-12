from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
            for i in range(start, len(nums)):
                # swap
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                # swap
                nums[start], nums[i] = nums[i], nums[start]

        result =[]
        backtrack(0)
        return result