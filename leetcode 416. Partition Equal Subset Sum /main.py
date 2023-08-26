from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        half_sum = int(sum(nums)/2)
        dp = [False] * (half_sum+1)
        dp[0] = True

        for num in nums:
            for i in range(half_sum, -1, -1):
                if dp[i] and i+num <= half_sum:
                    dp[num+i] = True
        return dp[half_sum]





"""
Given an integer array nums, 
return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""