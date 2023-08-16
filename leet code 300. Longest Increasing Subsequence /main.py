from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [float('inf')] * (len(nums)+1)
        dp[0] = nums[0]

        for i in range(1, len(dp)):
            length = 0
            for j in range(i, len(dp)):
                if nums[i]< nums[j]:
                    dp[i] = length+1
        return max(dp)

"""
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""