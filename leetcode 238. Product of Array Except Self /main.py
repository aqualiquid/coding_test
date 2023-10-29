from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        output = [1] * len(nums)

        since = 1
        for i in range(len(nums)):
            prefix[i] = since
            since *= nums[i]

        since = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = since
            since *= nums[i]

        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]
        return output