# main idea came from leetcode 416's 'partition equal subset' problem
#              Spos + Sneg = sum(nums)
#              Spos - Sneg = target
#Spos + Sneg + Spos - Sneg = sum(nums)+ target
#         2*Spos  = sum(nums)+ target
#                     Spos = (sum(nums)+target) / 2
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #if sum(nums) < target or (target+ sum(nums)) % 2 < 0 :
        total_sum= sum(nums)
        if total_sum < target or (target + total_sum) % 2 == 1 or (target + total_sum) < 0:
            return 0
        return self.targetSum(nums, (target + total_sum) // 2)

    def targetSum(self, nums, half_target)->int:
        dp = [0] * (half_target+1)
        dp[0] = 1    # since sum() = 0 has at least one
        for num in nums:
            for i in range(half_target, -1, -1):
                dp[i]+= dp[i-num]
        return dp[half_target]


"""
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' 
and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
\
Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 


    """