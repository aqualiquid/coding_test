"""
Time complexity of the previous solution (see 'main.py') is O(N^2).
In order to reduce the TC from O(N^2) to O(N*logN), I exploited 'bisect' library that made based-on the binary search.
'bisect_left' returns an index of the target parameter
-> from bisect import bisect_left
(e.g. [10, 9, 2, 5, 3, 7, 101, 18] -> ans: 4
"""
from bisect import bisect_left
from typing import List

class Solution_nlogn:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [float('inf') for _ in range(len(nums))]
        dp[0]=nums[0]

        for num in nums:
            idx = bisect_left(dp, num)
            dp[idx] = num
        return bisect_left(dp, float('inf'))





