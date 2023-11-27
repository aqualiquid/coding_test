from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            # check if there is previous consecutive number of the current index (same as initializing)
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest