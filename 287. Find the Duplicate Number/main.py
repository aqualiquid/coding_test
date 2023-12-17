from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        # Phase 1 : hare moves faster
        #  (i.e., moves the exact number of the index in nums)
        #    than tortoise
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        # Phase 2:
        # move tortoise to the start (i.e., nums[0])
        # if hare == tortoise, that's the REPEATED number
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare