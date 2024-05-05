from typing import List
from collections import defaultdict
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.picks = defaultdict(list)
        # append nums into the deafultdict()
        for i in range(len(nums)):
            self.picks[nums[i]].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.picks[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)