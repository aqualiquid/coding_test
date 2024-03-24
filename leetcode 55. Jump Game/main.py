from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        target = len(nums) - 1

        for i, num in enumerate(nums):
            if i > max_reach:  # If current index is beyond max reach, can't proceed further
                return False
            max_reach = max(max_reach, i + num)  # Update max reach
            if max_reach >= target:  # If max reach is at or beyond the last index, we can reach the end
                return True

        return False