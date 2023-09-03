from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def find_subsets(start, crnt:List[int]):
            result.append(crnt[:])
            for i in range(start, len(nums)):
                crnt.append(nums[i])
                find_subsets(i+1, crnt)
                crnt.pop()

        result = []
        find_subsets(0,[])
        return result