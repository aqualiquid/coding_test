from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        currnt_min = float('inf')

        while start < end:
            mid = (start + end) // 2
            currnt_min = min(currnt_min, nums[mid])

            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
        return min(currnt_min, nums[start])