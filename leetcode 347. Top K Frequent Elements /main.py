import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sorting  (generating bucket for each element of the range)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        # including 0, therfore, plus 1
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            # descending order
            for n in freq[i]:
                if n == len(res):
                    return res
                res.append(n)
        return res